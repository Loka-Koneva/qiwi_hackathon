import svelte from 'rollup-plugin-svelte';
import { config as configDotenv } from 'dotenv';
const svelteConfig = require('./svelte.config.js');  // it has to be a CommonJS import

configDotenv();

export default {
  // ...,
  plugins: [
    svelte({
      ...svelteConfig,
      // ...,
    }),
  ],
};