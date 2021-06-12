from collections import deque
# list1 = ["A", "B", "C", "D", "E"]
# list2 = ["G", "H", "I", "J", "K"]
# list4 = list1.copy()

# list4[1] = "A"

# print(list1)
# print(list4)


# list2.1lear()


# list1.append(list2)
# list1.extend(list2)
# list1.append(list2[0])
# list1.insert(0,list2)

# print(list1)



# list3 = ["G", "H", "X", "C", "B", "L", "K", "C"]
# sorted(list3)
# list3.sort()
# print(list3)

# print(list3.index("C"))
# print(list3.count("C"))
# list3.pop(1)
# list3.remove("C")
# print(list3)


# 5.1.1. リストをスタックとして使う
# stack = [2, 3, 8, 9]
# for n in range(11, 16, 2):
#     stack.append(n)

# print(stack)

# print(stack.pop())
# print(stack)

# 5.1.2. リストをキューとして使う
# queue = deque(["A", "B", "C"])
# queue = ["A", "B", "C"]
# queue.appendleft("D")
# queue.appendleft("D")

# queue.extendleft(["X", "Y", "Z"])
# print(queue)

# queue.popleft()
# queue.popleft()
# print(queue)

# 5.1.3. リストの内包表記

# squares = list(map(lambda x : x**2, range(10)))
# print(squares)


# squares2 = [x**2 for x in range(10)]

# print(squares==squares2)


# squares = list(map(lambda x : x**2 , range(10)))
# print(squares)

# monster =  input("モンスター名:")
# magic = input("呪文:")
# hero = input("英雄名:")
# damage =  int(input("ダメージ:"))

# str1="{0}は{1}をとなえた。{2}は{3}ポイントのダメージを受けた"
# print(str1.format(monster, magic, hero, damage))

# a = 12345
# b = 67890
# s = "{0:2}"
# print(s.format(a))

# print("{0}は英語で{1}といいます".format("猫","cat"))

# s = '{0:6}'
# t = '{0:6}'
# potal_code = s.format(123) + " - " + t.format(678)
# t = '{0:4}'
# print(s.format('abc'))
# print(potal_code)

# guest="佐藤、田中、山本"
# print(guest.replace("、", "様、", 2)) 

# lsta = ["A", "B", "C"]
# lstb = ["D", "E", "F"]
# lstc = lsta + ["Z"]
# lsta.extend("D")
# lsta.append(["E"])
# lsta.extend(lstb)
# lstc = list(map(lsta.extend(lsta)))
# lsta += lstb
# lsta.append("G")
# print(lsta[::2])
# print(len(lsta))
# print("->".join(lsta))

# w = "A, B, C, D, E"
# a = w.split(",")
# print(a)

# for n in reversed(lsta):
#     print(n)

# points = {"A":60, "B": 70, "C": 77, "D":82, "E": 85}
# n = 0
# for p in points[n]:
#     while p>80:
#         print(points[n]+'は合格')
#     else:
#         print(points[n]+'は不合格')

#     n += 1
    
# nums = [1, 2, 3, 4, 5, 6]
# for num in reversed(nums):
#     print(num, end=", ")
# else:
#     print("End")


# scores = [80, 100, 69]
# for score in scores:
#     if score < 70:
#         print("不合格")
#         break
# else:
#     print("合格")

# help(print)

# def sum(n):
#     if n > 0:
#         return n + sum(n-1)
#     return 0

# sum(3)

# def sum(n):
#     while n > 0:
#         return n + sum(n-1)
#     return 0

# print(sum(10))

# 位置引数
# def lunch(main, side, drink):
#     print('main:', main)
#     print('side:', side)
#     print('drink:', drink)

# # キーワード引数    
# def lunch(main="beef", drink="coffee", side="soup"):
#     print('main:', main)
#     print('side:', side)
#     print('drink:', drink)

# lunch("焼き肉", "レモンティー", "soba")


# print(list((map(lambda x : x*x, range(5)))))

# nums = []
# for n in range(5):
#     nums.append(n*n)
# print(nums)

# num1 = 0
# num2 = 0
# def add(x, y):
#     global num1, num2
#     num1 = x
#     num2 = y

# add(5,2)
# print(num1, num2)

# def test(n,m):
#     num = n
#     def test_in(m):
#         nonlocal num
#         num += m
#         # return n
    
#     test_in(m)
#     return num

# print(test(2,3)) 

def dog():
    def cat():
        # nonlocal pet
        pet = 'cat'  
    
    pet = 'dog'
    cat()
    print(pet)

dog()
