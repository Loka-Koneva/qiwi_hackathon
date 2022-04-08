import { browser } from '$app/env';
import { session } from "$app/stores";
export const browserGet = (key) => {
	if (browser) {
		const item = session[key];
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

export const getCurrentUser = async (refreshUrl) => {
	const response = await fetch(refreshUrl, {
		method: 'POST',
		mode: 'cors',
		credentials: 'same-origin',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			refresh: `${browserGet('refreshToken')}`
		})
	});
	const response_json = await response.json();
	if (response_json.access) {
		return {
			access: response_json.access,
			username: response_json.data.user,
			id: response_json
		}
	}
	return response_json;
}