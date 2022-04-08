<script>
    let items = [
        {'text': 'Вы выбираете услугу, указываете дату и время выполнения', 'icon': './chose.svg'},
        {'text': 'Вы оплачиваете выбранную услугу. Сумма замораживается на счету организации до выполнения работ', 'icon': './payment.svg'},
        {'text': 'Исполнитель оказывает услугу', 'icon': './ingeer.svg'},
        {'text': 'Вы подтверждаете и оцениваете выполнение работ. Оплата поступает на счет организации', 'icon': './ok.svg'}
    ]
</script>

<style>
    .how-it-works-header {
        font-family: 'Inter';
        font-style: normal;
        font-weight: 400;
        font-size: 75px;
        line-height: 116px;
        color: #845EC2;
        text-align: center;
        margin-top: auto;
        margin-bottom: 35px;
    }
    .howto-items {
        margin-top: 10px;
    }
    .howto-item-container{
        position: relative;
        height: 100%;
        text-align: center;
        margin-top: auto;
        margin-bottom: 30px;
        vertical-align: middle;
    }
    .howto-item-ellipse {
        left: 0;
        width: 210px;
        height: 210px;
        margin-right: 45px;
        display: inline-block;
        vertical-align: middle;
        background-color: #E5E5E5;
        border-radius: 50%;
        text-align: center;
    }
    .howto-item-icon {
        width: 180px;
        height: 180px;
    }
    .howto-text-container {
        vertical-align: middle; display: inline-block; text-align: start;
    }
    .howto-item-text {
        display: inline-block;
        vertical-align: middle;
        line-height: normal;
        width: 520px;
        font-size: x-large;
    }
</style>

<h1 class="how-it-works-header">Как это работает?</h1>

<div class="howto-items">
    {#each items as item}
        <div class="howto-item-container">
            <div class="howto-item-ellipse">
                <img src="{item.icon}" alt="{item.text}" class="howto-item-icon">
            </div>
            <div class="howto-text-container">
                <span class="howto-item-text">{item.text}</span>
            </div>
        </div>
    {/each}
</div>