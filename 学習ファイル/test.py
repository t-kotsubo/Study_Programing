# a = [6, 9, 12, 15, 4]
# for i in range(4):
#     print(a[i])

# your_name = input("名前:")

# print("あなたの名前は"+your_name)


# test_number = 100
# print(float(test_number) + 10)

# test = 0.5
# print(test)


# test ={ 'a':"1", 'b':'2', 'c':'3', 'd':'4' }
# test2 = ['a', 'b', 'c', 'd']
# print(test2[0:2])


# import testmod
# test_calss_1 = testmod.TestClass()

# def test_func(*args):
#     print(args)

# test_func('A','B','C','D','E')


# def test(arg1, arg2, arg3=3):

#     if arg3==1:
#         ans = arg1+arg2
#     if arg3==2:
#         ans = arg1-arg2
#     if arg3==3:
#         ans = arg1*arg2
#     print(ans)

# test(2,3)

# def test2(**kwargs):
#     print(kwargs)

# test2(No1='Kotsubo', No2='Takayuki')

# list_a = [5,2, 3, 2 ,4]



# print("list_aの値は",list_a,"です")

# list_b = list()
# list_b = list_a[::-1]

# print("list_bの値は",list_b,"です")

# list_a = ["a","b","c","d","e","f"]
# list_b = ["A","B","C","D","E","F"]
# list_c = ["5","7","1","3","4","2"]
# list_d = [1, 5, 6, 7 ,5]
# list_test = [74, 85, 69, 77, 81]
# high = [t for t in list_test if t>=80]

# print("テストの点は", list_test, "です。")
# print("80点以上は", high, "です。")
# print("80点以上の人数は", len(high), "人です。")


# a = [2, 3, 4 ,5, 10, 13, 25, 36]
# a.sort(reverse=True)
# more_than_ten = [t for t in a if t>=10]

# print("10以上の数", more_than_ten)
# print("10以上の数の個数", len(more_than_ten), "個")

# city = ['東京', '名古屋', '大坂', '京都', '福岡']
# high = [32, 28, 27, 26, 27]
# h1, h2, h3, h4, h5 =high

# print(h4)
# low =  [25, 21, 20, 19, 22]

# print("都市名データは", city, "です")
# print("最高気温データは", high, "です")
# print("最低気温データは", low, "です")
# for c, h, l in zip(city, high, low):
#     print(c,"の最高気温は", h, "最低気温は", l, "です。")

# tuple_a = (1,3,4,5,7,"a")
# for i in sorted(tuple_a, reverse=True):
#     print(i, end="")

# if all(tuple_a):
#     print("全て有効なデータです。")
# else:
#     print("ゼロもしくは無効なデータがあります。")

# sale1 = {"東京":100, "大坂":80, "名古屋":70, "札幌":60, "福岡":65}
# sale2 = {"岡山":50, "京都":60, "仙台":65, "浜松":50, "和歌山":45}

# if "浜松" in sale1 or sale2:
#     print("浜松のデータは存在します。")
# else: 
#     print("浜松のデータは存在しません。")

# if "甲府" in sale2:
#     print("甲府のデータは存在します。")
# else:
#     print("甲府のデータは存在しません。")

# def numbers(*args):
#     print(n)

# numbers(1,3,5,7,13,19)

# def fruits(**kwargs):
#     # dic = {**kwargs}
#     print(**kwargs)

# fruits(1='apple', 2='bom', 3='cigaretts') 

# n = 0
# while False:
#     n += 1
#     print(n, end=" ")
#     if n > 20:
#         break

# for n in range(50, 100):
#     if n % 10==0 :
#         continue
#     print(n, end=",")

# def exception_test(value_1, value_2):
 
#     print('＝＝＝＝計算開始＝＝＝＝')
 
#     result = 0
 
#     try:
#         result = value_1 + value_2
#     except:
#         print('計算出来ませんでした！')
#     finally:
#         print('計算終了')

#     return result    
 
# print(exception_test(100, 200))
# print(exception_test(100, '200'))

# def test():
#     return("test2")

# print(test())

# def test_func(**kwargs):
#     print(kwargs)

# test_func(A='a', B='b')

# class Test():
    
#     def __init__(self, foo, bar):
#         self.foo = foo
#         self.bar = bar

#     def abc(self):
#         print(foo)
#         print(bar)

# t = Test("test", "test2")
# t.abc()

# def sell(place, num=5):
#     print(place,'で', num,"店舗の販売が実施されました。")

# sell("山形", 3)

# sale = {}
# sale.update(sale1)
# sale.update(sale2)
# print(sorted(sale, reverse=True))


# def sell(a):
#     b=a * 5
#     print("aの5倍は", b,"です。" )


# sell(2)

# print("現在の売上データは", sale, "です")

# k = input("どの都市の売上データをお探しですか？")
# if k in sale:
#     print(k, "の売上データは", sale[k], "です。")    
# else:
#     print(k, "の売上データは存在しません。")


# print("最大値:", max(list_d))
# print("最小値:", min(list_d))
# print("合計値:", sum(list_d))
# print("平均値:", sum(list_d)/len(list_d))

# list_c.sort(reverse=True)
# print("降順", list_c)

# print("昇順",sorted(list_c))
# print("降順",sorted(list_c, reverse=True))

# # list_c = list(reversed(list_b))
# # list_c = list(list_b)
# dict_c = {}

# for e,f in zip(list_a, list_b):
#     dict_c.append(e,f)

# print(dict_c) 

# for i in iter(list_b):
#     print(i, end=" ")



# list_b = list(list_a)

# for d in zip(list_a, list_b):
#     print(d, end="")
 
# print()

# for e in enumerate(list_b):
#     print(e, end="")


# for f, g in zip(list_a, list_b):
#     print("小文字は", f, "大文字は", g,"です。")


# def test(**kwargs):
#     print(kwargs)

# test(A='あ', B="い", C="う")

#　◎クラス属性（クラス変数）とインスタンス変数
# class Sample:
#     commun = '共通'
#     name = ''
#     age = 0

#     @classmethod
#     def __init__(cls,name, age):
#         cls.name = name
#         cls.age = age
#     @classmethod
#     def test(cls):
#         print("名前は", cls.name, '年齢は', cls.age, 'です')

# # s = Sample('小壷', 43)
# s = Sample("小壷", 43)
# # print(s.name)
# # print(s.age)
# # print(Sample.commun)
# # s.test()

# print(Sample.name)

#　◎ラムダ式（無名関数、匿名関数）
# ans = lambda a, b : a*b
# print(ans(2,3))

# 継承
# class Parent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Children(Parent):
#     def __init__(self,name, age, country, city):
#         super().__init__(name, age)
#         self._country = country
#         self._city = city

#     def getCountry(self):
#         return self.country
    
#     def getCity(self):
#         return self.city


# chi1 = Children("加藤", 50, 'USA', "New York")

# chi1.getCountry
# chi1.getCity
# print(chi1.name)
# print(chi1._country)
# print(chi1._city)



# c = Children("小壷", 43, '日本', '東京')

# print(c.name)
# print(c.age)
# print(c.country)
# print(c.city)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Customer(Person):
    def __init__(self, name, age, adr, tel):
        super().__init__(name, age)

        self.adr = adr
        self.tel = tel

    def getAdr(self):
        return self.adr

    def getTel(self):
        return self.tel

c = Customer("小壷", 43, "Tokyo", "090-4643-4942")

# name = c.getName()
# age = c.getAge()
# print(c.name)
# print(c.age)
print(c.adr)
print(c.tel)