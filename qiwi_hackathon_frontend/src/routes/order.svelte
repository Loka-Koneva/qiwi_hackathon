<script context="module">
    import { getCurrentUser } from "../utils/index.js"
    import { goto } from "$app/navigation";
    import { page } from "$app/stores"
    export async function load() {
        const api_url = process.env.BASE_API_URL
        // const id = page.url.searchParams('email')
        const user_response = await getCurrentUser(`${api_url}/api/token/refresh/`, `${api_url}/api/user/`)
        if(!user_response.error && user_response.data.id) {
            return {props: {user: user_response.data, api_url: api_url}}
        } else {
            return {props: {user: {}, api_url: api_url}}
        }
        
    }
</script>

<script>
    export let user, api_url
    import { Button } from 'attractions'
    import { browserGet } from "../utils/index.js";
    function login() {
        // goto('/login');
    }
    async function logout() {
        const response = await fetch(`${api_url}/api/logout/`, {
            method: 'POST',
            mode: 'cors',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${user.tokens.access}`
            },
            body: JSON.stringify({
                refresh: browserGet('refreshToken')
            })
        })
        if(response.status == 204) {
            localStorage.removeItem('refreshToken');
            user = {}
            location.reload()
        }
    }
</script>

<header class="index-header">
    <h1 class="header-text">Платные услуги</h1>
    {#if !user.id}
        <div class="sign-in-btn">
            <Button filled on:click={login}>Войти</Button>
        </div>
    {:else}
        <div class="sign-in-btn">
            <Button danger filled on:click={logout}>Выйти</Button>
        </div>
    {/if}
    <img class="index-header-image" src="./order.png" alt="header"/>
</header>

<style>
    .index-header {
        position: relative;
        width: 100%;
        height: auto;
        text-align: center;
    }
    .index-header-image {
        width:100%;
        height:350px;
        object-fit: cover;
    }
    .index-header .sign-in-btn {
        position: absolute;
        top: 25px;
        right: 50px;
    }
    .header-text {
        position: absolute;
        width: 552px;
        height: 94px;
        left: 223px;
        top: 1px;
        font-family: 'Besley';
        font-style: normal;
        font-weight: 400;
        font-size: 60px;
        line-height: 109px;
        color: #FFFFFF
    }
</style>

<!-- markup (zero or more items) goes here -->