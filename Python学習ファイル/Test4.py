# price = 100
# print('りんごの価格は'+str(price)+'です。')
# print('りんごの価格は', price, 'です。')


# def hello(message, name='タカユキ'):
#     print(name + "さん、" + message)


# hello('こんにちは')
# def print_hand(hand, player_name='ゲスト'):
#         print(player_name +'は' +hand + 'を出しました')


# print_hand('グー','Taka')

# def add(a, b):
#     return a+b
#     print("Hello, World")

# sum = add(2,5)

# print(sum)

# def hello(name=input('名前を入力してください')):
#     if name =="":
#         return '名前を教えてください'
#     else:
#         return name+'さん、こんにちは'

# print(hello())

# import test

# print(test.Company)
# test.show_name()

# class Test:
#     pass

# test1 = Test()
# test1.name ="Taka"
# test1.address ="Tokyo"
# test1.age = 43

# test2 = Test()
# test2.name ="Toshi"
# test2.address ="Kanagawa"
# test2.age = 36

# print(test1.name, test2.name)

# from test import Child

# child1 = Child("Taka", 34, 169)
# child1.info()

# num = 10
# num *= 10
# print(num)

# lists = ["Apple", "Banana", 2, 5]

# lists.append('Peach')
# lists.insert(1,'Lemon')
# lists[4] = 'Grape'
# lists[3] = 'PineApple'


# # print(lists[1])

pairs = {3:"C",1:"A", 2:"B" }
pairs[3] = 'D'
pairs[4] = 'E'

# print(pairs[1])

for pair in pairs:
    print(str(pair)+'のペアは'+pairs[pair]+'です')