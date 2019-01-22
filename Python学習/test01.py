str = input("文字列を入力してください：")
old = input("どこを置換しますか？：")
new = input("置換する文字列を入力してください：")
res = str.find(old)

# if res != -1:
#     print(str,"の",res,"の位置に",old,"の文字がみつかりました。")
# else:
#     print(str,"に",old,"の文字がみつかりませんでした。")

if old in str:
    str.replace(old,new)
    print(str+"に置き換えました")
else:
    print(old+"という文字は見つかりません")



