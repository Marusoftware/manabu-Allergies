<script label="ts">
	import Nav from '../../components/Nav.svelte';
	let email = '';
	let password = '';
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
		<button class="btn w-96 m-2">サインイン</button>
		<p><a class="text-blue-600 underline" href="/signup">ここ</a>でアカウント登録ができます</p>
	</div>
</Nav>
