<script label="ts">
	import Nav from '../../components/Nav.svelte';
	import { goto } from '$app/navigation';
	import { signIn } from '../../store/auth';
	let isChecking = false;
	let email = '';
	let password = '';
	const handleClick = async () => {
		isChecking = true;
		try {
			await signIn(email, password);
			goto('/');
		} catch (error) {
			// @ts-ignore
			alert('おっと、サーバー側で何らかのエラーが発生しました。\n' + error.message);
		}
		isChecking = false;
	};
</script>

<Nav>
	<h1 class="text-4xl text-center m-4">サインイン</h1>
	<div class="flex flex-col items-center">
		<input
			bind:value={email}
			type="email"
			placeholder="Email"
			class="input input-bordered w-full max-w-sm m-2"
		/>
		<input
			bind:value={password}
			type="password"
			placeholder="Password"
			class="input input-bordered w-full max-w-sm m-2"
		/>
		{#if isChecking}
			<button class="btn btn-square loading w-96 m-2" />
		{:else}
			<button on:click={handleClick} class="btn w-96 m-2">サインイン</button>
		{/if}
		<p><a class="text-blue-600 underline" href="/signup">ここ</a>でアカウント登録ができます</p>
	</div>
</Nav>
