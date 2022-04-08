<script context="module">
    import { getCurrentUser } from "../utils/index.js"
    import { goto } from "$app/navigation";
    export async function load() {
        const api_url = process.env.BASE_API_URL
        const user_response = await getCurrentUser(`${api_url}/api/token/refresh/`, `${api_url}/api/user/`)
        if(!user_response.error && user_response.data.id) {
            return {props: {user: user_response.data}}
        } else {
            return {props: {user: {}}}
        }
        
    }
</script>

<script>
    export let user;
    import { Button } from "attractions"
    import Information from "../components/Information.svelte"
    function login() {
        goto('/login');
    }
</script>

<!-- markup (zero or more items) goes here -->

<header class="index-header">
    <h1 class="header-text">Платные услуги</h1>
    {#if !user.id}
        <div class="sign-in-btn">
            <Button filled on:click={login}>Войти</Button>
        </div>
    {:else}
        <div class="sign-in-btn">
            <Button filled on:click={logout}>Выйти</Button>
        </div>
    {/if}
    <img class="index-header-image" src="./index.jpeg" alt="header"/>
</header>
<section>
    {#if !user.id}
         <Information></Information>
    {:else}
         <span>wow</span>
    {/if}
</section>

<style>
    :global(body){
        background-image: none;
    }
    .index-header {
        position: relative;
        width: 100%;
        height: auto;
        text-align: center;
    }
    .index-header-image {
        height: 540px;
        object-fit: cover;
        width: 1440px;
    }
    .index-header .sign-in-btn {
        position: absolute;
        top: 35px;
        right: 200px;
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
        color: #554D76;
    }
</style>