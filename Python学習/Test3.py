# apple_price = 200
# input_num = input('購入する個数を入力してください。：')
# qty = int(input_num)
# price = apple_price * qty
# money = 1000
# balance = money - price

# if price < money:
#     print('リンゴを', qty , '個購入しました。', '\n値段は', price, '円です。', '\n残りは', balance, '円です')

# elif price == money:
#     print('リンゴを', qty ,'個購入しました。', '\n値段は', price, '円です。', '\nお金がなくなりました。')

# elif price > money:
#     print('リンゴを', qty ,'個購入しようしとしました。', '\n値段は', price, '円です。', '\nお金が足りません。')

# else :
#     print('不正なデータです。')

# print('現在の所持金は', balance, '円です。')

dic = {1:"A", 2:"B", 3:"C"}
num = 1

# print(dic[4])
# print(dic.get(4,"見つかりません"))
# del dic[2]

# print(dic.keys())
# print(dic.values())
# for a, b in dic.items():
#     print(a, b)

# print(dic)

# print(3 in dic)
# print(5 in dic)
# print("================")
# print(3 not in dic)
# print(5 not in dic)

test = {"A", "B", "C"}
test_set_1 = {'python', '-', 'izm', '.', 'com', 'python', 'izm'}
# print(test_set_1)

test_set_1.add('add')
test_set_1.remove('python')
test_set_1.update(test)

# print(test_set_1)

test_list = ["A", "B", "C", "D", "E"]
# print(test_list[0:4:3])
# print(test_list[::-1])
test_list[1:4] = ("b", "c", "d")
print(test_list)

print("\\12345")