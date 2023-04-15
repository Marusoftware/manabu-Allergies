<script lang="ts">
	import { onMount } from 'svelte';
	import Nav from '../../components/Nav.svelte';
	import { userApi } from '../../store/auth';
	import { writable } from 'svelte/store';
	import type { User } from '../../openapi/models';
	import { showNotification } from '../../util';
	const user=writable<User>({id:"",name:"",email:""});
	let password="******"
	let validate_email="";
	let validate_pasword=""
	onMount(async () => {
		user.set(await userApi.userMe())
	})
	async function updateName() {
		user.set(await userApi.userUpdateMe({userUpdate:{name:$user?.name}}))
	}
	async function updateEmail() {
		if(validate_email===$user.email){
			user.set(await userApi.userUpdateMe({userUpdate:{email:$user.email}}))
			location.href="#"
		} else {
			showNotification({type:"error", message:"メールアドレスが一致していません", timeout:3})
		}
	}
	async function updatePassword() {
		await userApi.userUpdateMe({userUpdate:{newPassword:password, oldPassword:validate_pasword}})
	}
</script>

<Nav>
	<h1 class="text-4xl text-center m-4">設定</h1>
	<div class="flex flex-col items-center">
		<div class="flex flex-row items-center">
			<input type="input" placeholder="Name" class="input input-bordered w-full max-w-sm m-2"  bind:value={$user.name} />
			<button class="btn" on:click={updateName}>更新</button>
		</div>
		<div class="flex flex-row items-center">
			<input type="email" placeholder="Email" class="input input-bordered w-full max-w-sm m-2" bind:value={$user.email} />
			<a class="btn" href="#email-modal">更新</a>
			<div class="modal" id="email-modal">
				<div class="modal-box">
					<h2 class="font-bold text-lg text-center">確認のためメールアドレスを入力してください</h2>
					<div class="flex flex-col items-center">
						<input
							type="email"
							placeholder="Email"
							class="input input-bordered w-full max-w-xl m-2"
							bind:value={validate_email}
						/>
					</div>
					<div class="modal-action">
						<a href="#" class="btn">キャンセル</a>
						<button class="btn" on:click={updateEmail}>確定</button>
					</div>
				</div>
			</div>
		</div>
		<div class="flex flex-row items-center">
			<input
				type="password"
				placeholder="Password"
				class="input input-bordered w-full max-w-sm m-2"
				bind:value={password}
			/>
			<a class="btn" href="#password-modal">更新</a>
			<div class="modal" id="password-modal">
				<div class="modal-box">
					<h2 class="font-bold text-lg text-center">確認のため古いパスワードを入力してください</h2>
					<div class="flex flex-col items-center">
						<input
							type="password"
							placeholder="Password"
							class="input input-bordered w-full max-w-xl m-2"
							bind:value={validate_pasword}
						/>
					</div>
					<div class="modal-action">
						<a href="#" class="btn">キャンセル</a>
						<button class="btn" on:click={updatePassword}>確定</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</Nav>
