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

export const getCurrentUser = async (refreshUrl, userUrl) => {
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
	const access_response = await response.json()
	if (access_response.access) {
		const user_response = await fetch(userUrl, {
			headers: {
				Authorization: `Bearer ${access_response.access}`
			}
		})
		if (user_response.status === 400) {
			const data = await user_response.json();
			const error = data.error[0];
			return {data: null, error: error};
		} else {
			const json = await user_response.json()
			return {data: json, error: null};
		}
		
	} else {
		return { data: {}, error: 'Время токена истекло'}
	}
}