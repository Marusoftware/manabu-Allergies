<script>
	import Alert from '../components/Alert.svelte';
	import '../app.css';
	import { destroyNotification, notifications } from '../util';
	import { fade } from 'svelte/transition';
</script>

{#if $notifications}
	<div class="absolute top-20 right-5 w-full max-w-xs z-50 isolation" >
		{#each $notifications as notification (notification.id)} 
			<div transition:fade class="pb-4">
				<Alert message={notification.message} type={notification.type} on:click={() => destroyNotification(notification.id)} />
			</div>
		{/each}
	</div>
{/if}
<slot />
