import { AuthApi, Configuration, type Token } from '../openapi';
import { get, writable } from 'svelte/store';
const accessToken=writable<Token>(undefined);
const config = new Configuration({
    basePath: '/api/v1',
    accessToken: async () => "Bearer "+get(accessToken).accessToken
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
}
