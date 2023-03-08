<script label="ts">
	import Nav from '../../components/Nav.svelte';
	import { AuthApi, Configuration } from '../../openapi';
	const config = new Configuration({
		basePath: '/api/v1',
		accessToken: async () => 'token' + Math.random()
	});
	const authApi = new AuthApi(config);
</script>

<Nav>
	<h1 class="text-4xl text-center m-4">サインアップ</h1>
	<div class="flex flex-col items-center">
		<input type="input" placeholder="Name" class="input input-bordered w-full max-w-sm m-2" />
		<input type="email" placeholder="Email" class="input input-bordered w-full max-w-sm m-2" />
		<input
			type="password"
			placeholder="Password"
			class="input input-bordered w-full max-w-sm m-2"
		/>
		<input
			type="password"
			placeholder="Confirm password"
			class="input input-bordered w-full max-w-sm m-2"
		/>
		<button class="btn w-96 m-2">サインアップ</button>
		<p><a class="text-blue-600 underline" href="/signin">ここ</a>でサインインできます</p>
	</div>
</Nav>
