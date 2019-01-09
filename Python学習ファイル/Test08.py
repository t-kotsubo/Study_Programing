# num = [[1,2],[3,4],[5,6]]
# num.append("1")
# num.append("2")
# num.append("3")
# num.append("4")

# for value1, value2 in num:
#     print(value1, value2)

# counter = 0

# while counter <10:
#     print(counter)
#     counter += 1

# for num in range(100):
#     if num % 10:
#         continue
#     print(num)

class Country:

    def __init__(self, country):
        self.country = country

    def show_Country():
        print(self.country)


class City(Country):

    def __init__(self, country, city):
        super().__init__(country)
        self.city = city

    def show_City():
        super().show_Country()
        print(self.city)

    @staticmethod
    def static_sample(x,y):
        return x + y

address_list = []
address_list.append(City('Japan', 'Tokyo'))
address_list.append(City('China', 'Beijin'))
address_list.append(City('Germany', 'Berlin'))

# print(address_list[0])

# for place in address_list:
#     place.show_City()

print(City.static_sample(10,5))