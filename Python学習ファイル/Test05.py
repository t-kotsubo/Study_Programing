class Test:
    def hello(self):
        print(self.name)
        print(self.age)


    def __init__(self, name, age):
        self.name = name
        self.age = age


test1 = Test("Taka",43)
# test1.name = "Taka"
# test1.age = 43


test1.hello()

