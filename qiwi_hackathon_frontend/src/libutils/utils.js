import { browser } from '$app/env';
export const browserGet = (key) => {
	if (browser) {
		const item = localStorage.getItem(key);
		if (item) {
			return item;
		}
	}
	return null;
};

export const browserSet = (key, value) => {
	if (browser) {
		localStorage.setItem(key, value);
	}
};