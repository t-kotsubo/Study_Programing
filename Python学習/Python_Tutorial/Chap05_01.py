# from collections import deque

# queue = deque(["A", "B", "C", "D", "E"])
# queue2 = deque(tuple("XYZ"))

# print(queue.pop())
# print(queue.popleft())
# print(queue2.pop())
# print(queue2.popleft())

# 5.3 タプルとシーケンス
# t = ()
# タプル・パッキング
# t = 1, "Hello", 0.25
# print(t)

# シーケンス・アンパッキング
# x, y, z = t
# print(x,y,z)

# 5.4 集合
# a = set('abracadabra')
# print(a)

# b = set('alacazam')
# c=set(['a', 'bc', 'de'])

# print(a)
# print(b)
# print(c)

# a = {x for x in 'abracadbaesdac' if not x == 'a'}
# print(a)

# l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
# print(l)

# del l[0]
# l.remove('Bob')
# print(l)

# 5.6 ループのテクニック

# items()メソッド
# dic = {1:"A", 2:"B", 3:"C"}

# for k, y in dic.items():
#     print(k, y)

# enumerate()関数
# for i, v in enumerate({'tic', 'tac', 'toe'}):
#     print(i, v)

# zip()関数
# quesitons = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# question_answer_sets = {}
# for question, answer in zip(quesitons, answers):
#     question_answer_sets[question] = answer

# print(question_answer_sets)

# reversed()関数
# for i in reversed(range(0,10,2)):
#     print(i)


# lst = ["A", "B", "C", "D", "A", "C"]

# lis_s =set(lst)
# print(lis_s)
# 結果： {'D', 'B', 'C', 'A'}

# t = tuple(lst)
# print(t)
# 結果：('A', 'B', 'C', 'D', 'A', 'C')

# リスト、タプル、セットの生成
# name = "ABCDE"
# l = list(name)
# t = tuple(name)
# s = set(name)

# print(l)
# print(t)
# print(s)
#　結果
# ['A', 'B', 'C', 'D', 'E']
# ('A', 'B', 'C', 'D', 'E')
# {'B', 'D', 'A', 'C', 'E'}

# sorted()関数
# fruits = set() 
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

# for f in sorted(set(basket)):
#     fruits.add(f)

# print(fruits)
# 結果
# {'apple', 'banana', 'pear', 'orange'}

# 5.7 同一、等価
# lst = [1, 2, 3]
# lst2 = [1, 2, 3]

# print(lst==lst2)
# print(lst is lst2)
# 結果：
# True
# False

string1, string2, string3 = 'A', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2
print(non_null)