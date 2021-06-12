import json
# print("hello", "Python", sep=", ", end=": ")
# repr("hello")


data = ["A", "B", "C", "D", "E"]
data2 = ["F", "G", "H", "I", "J"]


with open("json_test.json", "a") as file:
    json.dump(data2, file)    




