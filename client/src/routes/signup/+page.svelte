<script lang="ts">
	import Nav from '../../components/Nav.svelte';
	import { goto } from '$app/navigation';
	import { signUp } from '../../store/auth';
	import { field, form } from 'svelte-forms';
	import { max, required, email as _email, matchField, min } from 'svelte-forms/validators';
	import { filterMessage, showNotification } from '../../util';

	const name = field('name', '', [required(), max(1024)]);
	const email = field('email', '', [required(), _email(), max(1024)]);
	const password = field('password', '', [required(), min(6), max(1024)]);
	const confirm = field('confirm', '', [required(), matchField(password)]);
	const signupForm = form(name, email, password, confirm)
	
	async function submitSignup(e:Event) {
		e.preventDefault()
		await signupForm.validate()
		if(!$signupForm.valid){
			return
		}
		await signUp($name.value, $email.value, $password.value)
		goto('/');
	}

	
</script>

<Nav>
	<h1 class="text-4xl text-center m-4">サインアップ</h1>
	<form class="flex flex-col items-center" on:submit={submitSignup}>
		<input
			bind:value={$name.value}
			type="input"
			placeholder="Name"
			class="input input-bordered w-full max-w-sm m-2 {$name.valid ?"":"input-error"}"
		/>
		<div class="text-red-600 w-full max-w-sm">{$name.errors.map(filterMessage).join(", ")}</div>
		<input
			bind:value={$email.value}
			type="email"
			placeholder="Email"
			class="input input-bordered w-full max-w-sm m-2 {$email.valid ?"":"input-error"}"
		/>
		<div class="text-red-600 w-full max-w-sm">{$email.errors.map(filterMessage).join(", ")}</div>
		<input
			bind:value={$password.value}
			type="password"
			placeholder="Password"
			class="input input-bordered w-full max-w-sm m-2 {$password.valid ?"":"input-error"}"
		/>
		<div class="text-red-600 w-full max-w-sm">{$password.errors.map(filterMessage).join(", ")}</div>
		<input
			bind:value={$confirm.value}
			type="password"
			placeholder="Confirm password"
			class="input input-bordered w-full max-w-sm m-2 {$confirm.valid ?"":"input-error"}"
		/>
		<div class="text-red-600 w-full max-w-sm">{$confirm.errors.map(filterMessage).join(", ")}</div>
		<button type="submit" class="btn w-96 m-2">サインアップ</button>
		<p><a class="text-blue-600 underline" href="/signin">ここ</a>でサインインできます</p>
	</form>
</Nav>
