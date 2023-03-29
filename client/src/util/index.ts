import { writable } from "svelte/store"

export const filterMessage=(text:string)=>{
    text=text.replace("not_an_email", "正しいメールアドレスを入力してください。")
    text=text.replace("required", "この項目は必須です。")
    text=text.replace("min", "文字数が足りません。")
    text=text.replace("match_field", "パスワードが一致しません。")
    return text
}

interface Notification {
    id?:number,
    type: 'normal' | 'info' | 'success' | 'warning' | 'error',
    message:string,
    timeout?: number
}

export const notifications=writable<Notification[]>([])

export function showNotification(notification:Notification){
    const defaults={
        id :Math.floor(Math.random() * 10000),
        timeout:0
    }
    notification={
        ...defaults,
        ...notification
    }
    if(notification.timeout!==0){
        setTimeout(() => {
            destroyNotification(notification.id)
        }, (notification.timeout??0)*1000);
    }
    notifications.update((all) =>[notification, ...all])
    return notification.id
}
export const destroyNotification = (id?:number) => {
    notifications.update((all) => all.filter((t) => t.id !== id))
}