import svelte from 'rollup-plugin-svelte';
const svelteConfig = require('./svelte.config.js');  // it has to be a CommonJS import

export default {
  // ...,
  plugins: [
    svelte({
      ...svelteConfig,
      // ...,
    }),
  ],
};