class Shape:
    pass


class Square(Shape):

    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

obj1 = Square(1)
obj2 = Square(2)
obj3 = Square(3)

for n in Square.square_list:
    print(n.s1)

# class Shape():
#     def what_am_i(self):
#         print("I am a shape.")

# class Square(Shape):
#     square_list = []

#     def __init__(self, s1):
#         self.s1 = s1
#         self.square_list.append(self)

#     def calculate_perimeter(self):
#         return self.s1 * 4

#     def what_am_i(self):
#         super().what_am_i()
#         print("I am a Square.")


# a_square = Square(29)
# another_square = Square(93)

# for n in Square.square_list:
#     print(n.s1)
    