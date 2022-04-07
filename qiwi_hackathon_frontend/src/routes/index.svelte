<script>
    import { goto } from "$app/navigation";
    import { Button } from "attractions"
    function login() {
        goto('/login');
    }
</script>

<!-- markup (zero or more items) goes here -->

<header class="index-header">
    <h1 class="header-text">Платные услуги</h1>
    <div class="sign-in-btn">
        <Button filled on:click={login}>Войти</Button>
    </div>
    <div class="sign-up-btn">
        <Button filled danger>Регистрация</Button>
    </div>
    <div class="order-btn">
        <Button filled danger>Заказать</Button>
    </div>
    <img class="index-header-image" src="./index.jpeg" alt="header"/>
</header>
<section>
    <h1 class="how-it-works-header">Как это работает?</h1>
</section>

<style>
    /* your styles go here */
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
    .index-header .order-btn {
        position: absolute;
        width: 280px;
        height: 67px;
        top: 444px;
        left: 137px;
    }
    .index-header .sign-in-btn {
        position: absolute;
        top: 35px;
        right: 200px;
    }
    .index-header .sign-up-btn {
        position: absolute;
        top: 35px;
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
        color: #554D76;
    }
    .how-it-works-header {
        font-family: 'Inter';
        font-style: normal;
        font-weight: 400;
        font-size: 75px;
        line-height: 116px;
        color: #845EC2;
        position: absolute;
        margin-left: 30%;
        margin-right: 30%;
        margin-top: auto;
    }
</style>