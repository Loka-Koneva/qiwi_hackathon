import adapter from '@sveltejs/adapter-auto';
import preprocess from 'svelte-preprocess';
import makeAttractionsImporter from 'attractions/importer.js';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
import { config as configDotenv } from 'dotenv';
configDotenv();

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: [
		preprocess({
			scss: {
				importer: makeAttractionsImporter({
					themeFile: path.join(__dirname, 'static/css/theme.scss'),
				}),
				includePaths: [path.join(__dirname, './static/css')],
			},
			replace: [['process.env.BASE_API_URL', JSON.stringify(process.env.BASE_API_URL)]],
		})
	],
	kit: {
		adapter: adapter()
	}
};

export default config;
