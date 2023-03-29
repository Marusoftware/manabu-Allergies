<script lang="ts">
	import Nav from '../../components/Nav.svelte';
</script>

<Nav>
	<h1 class="text-4xl text-center m-4">設定</h1>
	<div class="flex flex-col items-center">
		<div class="flex flex-row items-center">
			<input type="input" placeholder="Name" class="input input-bordered w-full max-w-sm m-2" />
			<button class="btn">更新</button>
		</div>
		<div class="flex flex-row items-center">
			<input type="email" placeholder="Email" class="input input-bordered w-full max-w-sm m-2" />
			<a class="btn" href="#my-modal-2">更新</a>
			<div class="modal" id="my-modal-2">
				<div class="modal-box">
					<h2 class="font-bold text-lg text-center">確認のためパスワードを入力してください</h2>
					<div class="flex flex-col items-center">
						<input
							type="password"
							placeholder="Password"
							class="input input-bordered w-full max-w-xl m-2"
						/>
					</div>
					<div class="modal-action">
						<a href="#" class="btn">キャンセル</a>
						<a href="#" class="btn">確定</a>
					</div>
				</div>
			</div>
		</div>
		<div class="flex flex-row items-center">
			<input
				type="password"
				placeholder="Password"
				class="input input-bordered w-full max-w-sm m-2"
			/>
			<a class="btn" href="#my-modal-2">更新</a>
			<div class="modal" id="my-modal-2">
				<div class="modal-box">
					<h2 class="font-bold text-lg text-center">確認のためパスワードを入力してください</h2>
					<div class="flex flex-col items-center">
						<input
							type="password"
							placeholder="Password"
							class="input input-bordered w-full max-w-xl m-2"
						/>
					</div>
					<div class="modal-action">
						<a href="#" class="btn">キャンセル</a>
						<a href="#" class="btn">確定</a>
					</div>
				</div>
			</div>
		</div>
	</div>
</Nav>
