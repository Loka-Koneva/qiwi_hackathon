<script context="module">
    export async function load(){
        return {props: {api_url: process.env.BASE_API_URL}}
    }
</script>
<script>
    export let api_url;
    import { goto } from '$app/navigation';
    import { Card, Button, FormField, TextField } from 'attractions'
    import { browserGet, browserSet } from "../libutils/utils.js"
    let email = ''
    let password = ''
    let errors = null;
    async function submit () {
        const response = await fetch(`${api_url}/api/login/`, { 
                method: 'POST',
                mode: 'cors',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: email,
                    password: password
                })
            }
        )
        if(response.status == 201) {
            let json = await response.json()
            browserSet('refreshToken', json.user.tokens.refresh)
            await goto('/')
        } else {
        }
    }
</script>

<div class="login-card">
    <Card>
        <!-- <form on:submit|preventDefault={submit}> -->
            <FormField name="e-mail" help="Введите e-mail" required>
                <TextField type="text" bind:value={email} />
            </FormField>
    
            <FormField name="Пароль" help="Введите пароль" required>
                <TextField type="password" bind:value={password}/>
            </FormField>
            <Button filled on:click={submit} danger>Войти</Button>
        <!-- </form> -->
    </Card>    
</div>

<style>
    :global(body){
        height: 100vh;
        background-image: url('./login-background.jpg');
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        overflow: hidden;
        position: relative;
    }
    .login-card {
        position: absolute;
        width: 665px;
        height: 834px;
        left: 0;
        right: 0;
        margin-left: auto;
        margin-right: auto;
        top: 30%;
    }
</style>