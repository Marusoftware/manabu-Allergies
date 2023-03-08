import { sveltekit } from '@sveltejs/kit/vite';
import type { UserConfig } from 'vite';

const config: UserConfig = {
	plugins: [sveltekit()],
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	},
	server:{
		proxy: {
			"/api/v1/": {
			target:"http://localhost:8000/",
			changeOrigin: true,
			rewrite: (path:string) => path.replace('/api/v1', '')
			}
		}
	}
};

export default config;
