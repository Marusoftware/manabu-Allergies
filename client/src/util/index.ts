export const filterMessage=(text:string)=>{
    text=text.replace("not_an_email", "正しいメールアドレスを入力してください。")
    text=text.replace("required", "この項目は必須です。")
    return text
}