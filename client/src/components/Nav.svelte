<script lang="ts">
	import { goto } from '$app/navigation';
	import { accessToken, signOut } from '../store/auth';

	async function signout(){
		await signOut()
		accessToken.set(null)
	}
</script>

<div class="navbar bg-base-100">
	<div class="flex-none">
		<label for="my-drawer" class="btn btn-square btn-ghost">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				class="inline-block w-5 h-5 stroke-current"
				><path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M4 6h16M4 12h16M4 18h16"
				/></svg
			>
		</label>
	</div>
	<div class="flex-1">
		<a href="/" class="btn btn-ghost normal-case text-xl">Manabu Allergies</a>
	</div>
	<div class="flex-none">
		{#if $accessToken===null}
			<button class="btn btn-ghost normal-case hidden sm:block" on:click={() => goto('/signin')}
				>サインイン</button
			>
			<button class="btn btn-ghost normal-case hidden sm:block" on:click={() => goto('/signup')}
				>サインアップ</button
			>
		{:else}
			<button class="btn btn-ghost normal-case hidden sm:block" on:click={signout}
				>サインアウト</button
			>
		{/if}
		<div class="dropdown dropdown-bottom dropdown-left sm:hidden">
			<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
			<!-- svelte-ignore a11y-label-has-associated-control -->
			<label tabindex="0" class="btn btn-square btn-ghost">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					class="inline-block w-5 h-5 stroke-current"
					><path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"
					/></svg
				>
			</label>
			<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
			<ul tabindex="0" class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52">
				<li><a href="/signin">サインイン</a></li>
				<li><a href="/signup">サインアップ</a></li>
			</ul>
		</div>
	</div>
</div>
<div class="drawer">
	<input id="my-drawer" type="checkbox" class="drawer-toggle" />
	<div class="drawer-content">
		<slot />
	</div>
	<div class="drawer-side">
		<label for="my-drawer" class="drawer-overlay" />
		<ul class="menu p-4 w-80 bg-base-100 text-base-content">
			<li><a href="/ranking">ランキング</a></li>
			<li><a href="/reference">図鑑</a></li>
			<li><a href="/scan">スキャン</a></li>
			<li><a href="/settings">設定</a></li>
		</ul>
	</div>
</div>
