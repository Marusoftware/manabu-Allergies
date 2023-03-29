<script lang="ts">
	// @ts-nocheck

	import Nav from '../../components/Nav.svelte';
	let preview, fileinput;
	const onFileSelected = (e) => {
		let image = e.target.files[0];
		let reader = new FileReader();
		reader.readAsDataURL(image);
		reader.onload = (e) => {
			preview = e.target.result;
		};
	};
</script>

<Nav>
	<h1 class="text-4xl text-center m-4">スキャン</h1>
	<div class="flex flex-col">
		<input
			class="hidden"
			type="file"
			accept="image/*"
			on:change={(e) => onFileSelected(e)}
			bind:this={fileinput}
		/>
		<div class="m-4 flex flex-row justify-between">
			<button class="btn" on:click={() => fileinput.click()}>画像を選択</button>
			{#if preview != null}
				<button class="btn">画像を送信</button>
			{:else}
				<button class="btn btn-disabled" on:click={() => {}}>画像を送信</button>
			{/if}
		</div>
		<img class="m-4" src={preview} alt="" />
	</div>
</Nav>
