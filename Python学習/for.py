# リストの宣言及び要素の追加
list = []
list.append("A")
list.append("B")
list.append("F")
list.append("O")

for i in list:
    print(i)

# 2次元配列
test_list_1 = [['https', 'www'], ['python-izm', 'com']]
 
for value in test_list_1:
    print(value)
 
 # リストからループで複数の要素を取り出して処理する場合
for value_1, value_2 in test_list_1:
    print(value_1, value_2)

# for i in range(30):
#     if i%2==0:
#         continue
#     print(i)
#     if i==13:
#         break

