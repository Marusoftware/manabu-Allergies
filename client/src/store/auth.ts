import { AuthApi, Configuration } from '../openapi';
const config = new Configuration({
    basePath: '/api/v1',
    accessToken: async () => 'token' + Math.random()
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
    return res;
}
export const signOut = async () => {
    await authApi.authSignout()
}
