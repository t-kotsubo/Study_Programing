# str = input("文字列を入力してください：")
# old = input("どこを置換しますか？：")
# new = input("置換する文字列を入力してください：")
# res = str.find(old)

# if res != -1:
#     print(str,"の",res,"の位置に",old,"の文字がみつかりました。")
# else:
#     print(str,"に",old,"の文字がみつかりませんでした。")

# if old in str:
#     renew=str.replace(old,new)
#     print(renew+"に置き換えました")
# else:
#     print(old+"という文字は見つかりません")

# name = "小壷 崇行"

# rename = name.replace("壷", "壺")
# print(rename)

# name = "animal"

# try:
#     i = name.index('n')
#     print(i)
# except:
#     print("Not found.")


# print('彼女は"そうだね"と言った。')
# print("LINE1\nLINE2\nLine3")

# test_list = ["a", "b", "c", "d", "e"]
# print(test_list[0:3])
# test_word = "Hello_Everyone"
# print(test_word[0:-2])

# print(test_word[6:])

# 1.
# str = "カミュ"
# print(str[0])
# print(str[1])
# print(str[2])

# 2.
# input1 = input("何を：")
# input2 = input("誰に：")
# text = "私は昨日{}を書いて、{}に送った".format(input1,input2)
# print(text)

#3. 
# text = "hello everyone!"
# print(text.upper())

#4. 
# text = "どこで？,誰が？,いつ？"
# n = text.split(",")
# print(n)

# lst = "Where now? Who now? When now?".split(" ")
# print(lst)

#5. 
# lst = ["The", "fox", "jumped", "over", "the", "fence","."]
# ans = " ".join(lst)
# ans = ans[0: -2] + "."
# print(ans)

#6.
# test = "A screaming comes across the sky."
# test = test.replace("s", "$")
# print(test)

#7.
# test = "Hemingway"
# print(test.index("m"))

#8.
# test = "I like \"Seven Samurai\""
# print(test)

#9.
# lst = ["there", "there", "there"]
# print("".join(lst))
# lst2 = "there" * 3
# print(lst2)

# qs = ["What is yoiur name?",
#       "What is your fav.color?",
#       "What is your quest?"]

# n = 0
# while True:
#     print("Type q to quit")
#     a = input(qs[n])
#     if a == "q":
#         break
#     n = (n+1) % 3

word = "TEST"
lst =list(word)
print(lst)


