import { AuthApi, Configuration, UserApi, type Middleware, type ResponseContext, type Token } from '../openapi';
import { get, writable } from 'svelte/store';
import { showNotification } from '../util';

class APIExceptionHandlerMiddleware implements Middleware{
    async post(context: ResponseContext): Promise<void | Response> {
        if(context.response.ok){
            return
        }
        const json=await context.response.json()
        if(typeof json.detail === 'string') {
            showNotification({message:json.detail, type:"error", timeout:3})
        } else {
            showNotification({message:"何らかの問題が発生しました", type:"error", timeout:3})
        }
    }
}

export const accessToken=writable<Token|null>(null);
const config = new Configuration({
    basePath: '/api/v1',
    accessToken: async () => "Bearer "+get(accessToken)?.accessToken,
    middleware: [new APIExceptionHandlerMiddleware]
});
export const authApi = new AuthApi(config);
export const userApi = new UserApi(config);
export const signUp = async (name: string, email: string, password: string) => {
    const res = await authApi.authSignup({
        userCreate: {
            name: name,
            email: email,
            password: password,
        },
    })
    return res;
}
export const signIn = async (username: string, password: string) => {
    const res = await authApi.authSignin({
        username: username,
        password: password
    })
    accessToken.set(res)
    return res;
}
export const signOut = async () => {
    await authApi.authSignout()
    accessToken.set(null)
}
