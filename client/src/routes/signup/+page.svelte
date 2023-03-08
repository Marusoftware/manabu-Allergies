<script label="ts">
	import Nav from '../../components/Nav.svelte';
	let name = '';
	let email = '';
	let password = '';
	let confirm = '';
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
		<input
			bind:value={confirm}
			type="password"
			placeholder="Confirm password"
			class="input input-bordered w-full max-w-sm m-2"
		/>
		<button class="btn w-96 m-2">サインアップ</button>
		<p><a class="text-blue-600 underline" href="/signin">ここ</a>でサインインできます</p>
	</div>
</Nav>
