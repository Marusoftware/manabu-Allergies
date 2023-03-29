<script lang="ts">
	import { form, field } from 'svelte-forms';
	import { max, required, email as _email } from 'svelte-forms/validators';
	import { signIn } from '../../store/auth';
	import Nav from '../../components/Nav.svelte';

	const email = field('email', '', [required(), _email(), max(1024)]);
	const password = field('password', '', [required(), max(1024)]);
	const loginForm = form(email, password);

	async function submitSignin(e:Event){
		e.preventDefault()
		await loginForm.validate()
		if(!$loginForm.valid){
			return
		}
		await signIn($email.value, $password.value)
	}
</script>

<Nav>
	<h1 class="text-4xl text-center m-4">サインイン</h1>
	<form class="flex flex-col items-center" on:submit={submitSignin}>
		<input
			id="email"
			bind:value={$email.value}
			type="email"
			placeholder="Email"
			class="input input-bordered w-full max-w-sm m-2 {$email.valid ?"":"input-error"}"
		/>
		<input
			bind:value={$password.value}
			type="password"
			placeholder="Password"
			class="input input-bordered w-full max-w-sm m-2 {$password.valid ?"":"input-error"}"
		/>
		
		<button type="submit" class="btn w-96 m-2">サインイン</button>
		<p><a class="text-blue-600 underline" href="/signup">ここ</a>でアカウント登録ができます</p>
	</form>
</Nav>
