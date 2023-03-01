<script label="ts">
	import Nav from '../../components/Nav.svelte';
	const items = [
		{ title: '卵', content: 'アレルギーアレルギーアレルギー' },
		{ title: '鶏', content: 'アレルギーアレルギーアレルギー' },
		{ title: '小麦', content: 'アレルギーアレルギーアレルギー' },
		{ title: '牛乳', content: 'アレルギーアレルギーアレルギー' },
		{ title: 'くるみ', content: 'アレルギーアレルギーアレルギー' },
		{ title: 'ナッツ', content: 'アレルギーアレルギーアレルギー' },
		{ title: '魚', content: 'アレルギーアレルギーアレルギー' },
		{ title: 'いくら', content: 'アレルギーアレルギーアレルギー' },
		{ title: 'カニ', content: 'アレルギーアレルギーアレルギー' },
		{ title: '花粉', content: 'アレルギーアレルギーアレルギー' }
	];
</script>

<Nav>
	<h1 class="text-4xl text-center m-4">図鑑</h1>
	<div class="flex flex-row flex-wrap justify-center">
		{#each items as item}
			<div class="card w-96 bg-base-100 shadow-xl m-8">
				<figure>
					<img src="/favicon.png" alt="Shoes" />
				</figure>
				<div class="card-body">
					<h2 class="card-title">
						{item.title}
					</h2>
					<p>{item.content}</p>
				</div>
			</div>
		{/each}
	</div>
</Nav>
