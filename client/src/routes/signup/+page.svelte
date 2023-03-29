<script label="ts">
	import Nav from '../../components/Nav.svelte';
	import { goto } from '$app/navigation';
	import { signUp } from '../../store/auth';
	let isChecking = false;
	let isChecked = false;
	let name = '';
	let email = '';
	let password = '';
	let confirm = '';
	const handleClick = async () => {
		isChecking = true;
		isChecked = true;
		if (name != '' && email != '' && password.length > 5 && password == confirm) {
			try {
				await signUp(name, email, password);
				goto('/');
			} catch (error) {
				// @ts-ignore
				alert('おっと、サーバー側で何らかのエラーが発生しました。\n' + error.message);
			}
		}
		isChecking = false;
	};
</script>

<Nav>
	<h1 class="text-4xl text-center m-4">サインアップ</h1>
	<div class="flex flex-col items-center">
		<input
			bind:value={name}
			type="input"
			placeholder="Name"
			class="input input-bordered w-full max-w-sm m-2"
		/>
		{#if name == '' && isChecked}
			<div class="text-red-600 w-full max-w-sm">このフィールドは必須です。</div>
		{/if}
		<input
			bind:value={email}
			type="email"
			placeholder="Email"
			class="input input-bordered w-full max-w-sm m-2"
		/>
		{#if email == '' && isChecked}
			<div class="text-red-600 w-full max-w-sm">このフィールドは必須です。</div>
		{/if}
		<input
			bind:value={password}
			type="password"
			placeholder="Password"
			class="input input-bordered w-full max-w-sm m-2"
		/>
		{#if password == '' && isChecked}
			<div class="text-red-600 w-full max-w-sm">このフィールドは必須です。</div>
		{:else if password.length < 6 && isChecked}
			<div class="text-red-600 w-full max-w-sm">6文字以上入力してください。</div>
		{/if}
		<input
			bind:value={confirm}
			type="password"
			placeholder="Confirm password"
			class="input input-bordered w-full max-w-sm m-2"
		/>
		{#if confirm == '' && isChecked}
			<div class="text-red-600 w-full max-w-sm">このフィールドは必須です。</div>
		{:else if password != confirm && isChecked}
			<div class="text-red-600 w-full max-w-sm">パスワードと一致しません。</div>
		{/if}
		{#if isChecking}
			<button class="btn btn-square loading w-96 m-2" />
		{:else}
			<button on:click={handleClick} class="btn w-96 m-2">サインアップ</button>
		{/if}
		<p><a class="text-blue-600 underline" href="/signin">ここ</a>でサインインできます</p>
	</div>
</Nav>
