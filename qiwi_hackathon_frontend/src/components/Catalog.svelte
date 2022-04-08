<script>
import { goto } from "$app/navigation";

    export let user_id = null
    export let services = [];
    function orderService(id) {
        goto(`/order?id=${id}`)
    }
</script>


<div class="container">
    <h1 class="catalog-header">Выбрать услугу</h1>
    <div class="catalog-container">
        {#each services as item}
            <div class="service-card" on:click|preventDefault={() => orderService(item.uid)}>
                <div class="service-price-container">
                    <span class="service-price">{item.cost}</span>
                </div>
                <img class="service-icon" src="./{item.icon}" alt="service-icon">
                <div class="service-name-container">
                    <span class="service-name">{item.name}</span>
                </div>
            </div>
        {:else}
            <h1 class="empty-catalog">Пока никакие услуги недоступны</h1>
        {/each}
    </div>
</div>

<style>
    .container {
        padding-left: 15%;
        padding-right: 10%;
    }
    .catalog-header {
        font-family: 'Inter';
        font-style: normal;
        font-weight: 400;
        font-size: 36px;
        line-height: 44px;

        /* identical to box height */

        color: #4B4453;
    }
    .empty-catalog {
        font-family: 'Inter';
        font-style: normal;
        font-weight: 346;
        font-size: 20px;
        line-height: 44px;
        color: #4b4453d6;
    }
    .catalog-container {
        display: flex;
        flex-wrap: wrap;
        text-align: left;
        position: relative;
        height: 100%;
    }
    .service-card { 
        flex: 0 0 30%;
        width: 404px;
        height: 263px;
        background: #E5E5E5;
        margin-right: 10px;
        margin-bottom: 10px;
        position: relative;
        cursor: pointer;
    }
    .service-price-container {
        display: block;
        width: 100%;
    }
    .service-price {
        display: block;
        text-align: right;
        margin-right: 15px;
        margin-top: 15px;
        font-family: 'Inter';
        font-style: normal;
        font-weight: 400;
        font-size: 24px;
        line-height: 29px;
        color: #845EC2;
    }
    .service-icon {
        display: block;
        margin-left: 30%;
        margin-right: 30%;
    }
    .service-name-container {
        display: block;
        text-align: center;
        position: absolute;
        bottom: 10px;
        width: 100%;
    }
    .service-name {
        text-align: center;
        font-family: 'Inter';
        font-style: normal;
        font-weight: 400;
        font-size: 22px;
        line-height: 27px;

        /* identical to box height */

        color: #4B4453;
    }
</style>
