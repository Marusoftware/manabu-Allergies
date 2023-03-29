import { AuthApi, Configuration, type Middleware, type ResponseContext, type Token } from '../openapi';
import { get, writable } from 'svelte/store';

class APIExceptionHandlerMiddleware implements Middleware{
    async post(context: ResponseContext): Promise<void | Response> {
        try {
            const json=await context.response.json()
            if (json.detail) {
                alert(json.detail)
            }
        } catch (error) {
            console.log(error)
        }
    }
}

const accessToken=writable<Token|null>(null);
const config = new Configuration({
    basePath: '/api/v1',
    accessToken: async () => "Bearer "+get(accessToken)?.accessToken,
    middleware: [new APIExceptionHandlerMiddleware]
});
const authApi = new AuthApi(config);
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
