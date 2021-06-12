class A:

    def __init__(self,x):
        self.__x = x

    def getX(self):
        return self.__x
    

    def setX(self,x):
        self.__x = x

    
a = A(10)
# print(a.x)

print(a.getX())

print(_)