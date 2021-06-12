# class Test:
#     pass



# t = Test()
# t.a = "test"
# print(t.a)

numbers = ['1', '2', 'three', 4]
sum = 0
for n in numbers:
    try:
     sum += int(n)
    except ValueError:
        pass
print(sum)

