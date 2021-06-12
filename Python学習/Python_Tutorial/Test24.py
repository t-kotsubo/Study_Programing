import json
# ファイルの入出力
# with open("greeting.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# dict = {"name": "tarou", "age":23, "gender":"man"}
# enc = json.dumps(dict)
# print(dict)
# print(type(dict))
# print(enc)
# print(type(enc))
# # デコード
# dec = json.loads(enc)
# print(dec)
# print(type(dec))

menu = [
    {'name':'ハンバーガー', 'price':100, 'calorie': 260},
    {'name':'チーズバーガー', 'price':130, 'calorie':310},
    {'name':'フライドチキン', 'price':150, 'calorie':420}
]

print(json.dumps(menu))

# with open("menu.json", "w") as file:
#     json.dump(menu, file)

# with open("menu.json", "w") as file:
#     json.dump(menu, file, indent=4)

# with open('menu.json','r') as file:
#     print(json.load(file), sep=",\n")

