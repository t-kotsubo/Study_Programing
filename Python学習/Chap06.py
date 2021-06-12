# names = "Nori", "Taka", "Yoshi"

# print(names)

# name1, name2, name3 = names
# print(name1)


# name1, name2 = "Nori", "Taka"
# print(name2)

# タプルのリスト
# lst = []
# lst = [('blue', 'hat'),('red', 'shart'),('green', 'socks')]
# # lst = ('blue', 'hat')
# print(lst[2][1])


# for index, item in enumerate(lst, 1):
#     print('{} : {}'.format(index, item))

# 可変長引数
# def display_list(*name):
#     print(name)


# display_list("Tokyo", "Osaka", "Kyoto", "Kanagawa")

# def add_test(*num):
#     total = 0
#     for n in num:
#         total += n
#     print(total)

# add_test(2,3,5,3)

# 集合
# t = ('a', 'b', 'c', 'd', 'a')
# n = {'a', 'b', 'c', 'd', 'a'}

# n |= {'x', 'y', 'z'}
# print(n)

# n -= {'c'}
# print(n)

# print("タプル", t[::-1])
# print("集合", n[1])

# set_sample = set()

# zoo1 = {'lion', 'tiger', 'elephant', 'giraffe'}
# zoo2 = {'elephant', 'panda', 'snake', 'lion'}

# print(zoo1 & zoo2)
# print(zoo1 | zoo2)
# print(zoo1 - zoo2)
# print(zoo1 ^ zoo2)

# 辞書
# topping = {'bacon':210, 'mushroom':140, 'onion':100, 'tomato':130}
# print(topping['mushroom'])

# for key in topping:
#     print(key, end=", ")

# for key, value in topping.items():
#     print(key, value, end=", ")

# topping['bacon'] =250
# del topping['onion']
# topping['eggplant'] =150


# for key, value in topping.items():
#     print(key, value, end=", ")


# sample = "SAMPLE"

# for i, item in enumerate(sample, 1):
#     print(i, item, end=", ")

# lst = [x**2 for x in range(10) if x**2%2!=0]
# print(lst)

# lst1 = {key:value for in enumerate("SAMPLE")


# lst2 = {kye:value for kye, value in enumerate("SAMPLE",1)}
# print(lst2)

# list3 = ["Fizz" if x%3 ==0 else x for x in range(1,10)]
# print(list3)

# list4 = [x*y for x in range(1,10) for y in range(1,5)] 
# print(list4)

# num1 = [x for x in range(1000)]
# num2 = (x for x in range(1000))

# # print(num1)
# # for n in num
# #     print(n)

# for n in num2:
#     print(n)

# yield文

# def fizzbuzz(n):
#     for x in range(1, n):
#         if x % 15 == 0:
#             yield 'FizzBuzz'
#         elif x % 5 == 0:
#             yield 'Buzz'
#         elif x % 3 == 0:
#             yield 'Fizz'
#         else:
#             yield x


# print(list(fizzbuzz(100)))




