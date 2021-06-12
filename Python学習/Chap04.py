# 4.7.3 任意引数リスト

# def concat(*args, sep="/"):
#     print(sep.join(args))


# concat("A", "B", "C")



# def concat(*args, w=","):
#     print(w.join(args))

# concat("A", "B", "C")

# 4.7.4 引数リストのアンパック
# lst = ["A", "B", "C", "D", "E"]
# print(lst)
# print(range(lst))
# a = [0, 10, 2]
# mylist = list(range(*a))

# print(mylist)

# 4.7.5 ラムダ式
# def makeincrementor(n):
#     return  lambda x : x + n 


# f = [makeincrementor(10)]
# # makeincrementor(20)

# f(0)
# f(1)
# print(f)

# def lambda_sample(a):
#     return lambda b : a + b

# ans = lambda_sample(3)
# print(ans(2))
# print(ans(1))

# ans = lambda_sample(5,7)
# print(ans)

# greeting = (lambda : "Hello")
# print(greeting())

# greeting = (lambda: 'hello')()
# print(greeting)

# sample = lambda s : s + "World!"

# print(sample("Hello, "))

test = lambda s : "Hello!" + s

print(test("Taka."))


   