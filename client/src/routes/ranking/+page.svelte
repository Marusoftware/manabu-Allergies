<script label="ts">
	import Nav from '../../components/Nav.svelte';
	const items = ['aaa', 'bbb', 'ccc'];
</script>

<Nav>
	<h1 class="text-4xl text-center m-4">ランキング</h1>
	<ul class="flex flex-col items-center m-4">
		{#each items as item, i}
			<li class="card bg-base-100 shadow-xl m-4">
				<span class="text-4xl m-4">{i + 1}位 {item}</span>
			</li>
		{/each}
	</ul>
</Nav>
