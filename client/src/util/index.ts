export const filterMessage=(text:string)=>{
    text=text.replace("not_an_email", "正しいメールアドレスを入力してください。")
    text=text.replace("required", "この項目は必須です。")
    text=text.replace("min", "文字数が足りません。")
    text=text.replace("match_field", "パスワードが一致しません。")
    return text
}