import random

# choice関数
# flavor = ["バニラ", "チョコレート", "ストロベリー"]

# print(random.choice(flavor))

# shuffle関数

sample = ["A", "B", "C", "D", "E"]
for i in range(5):
    random.shuffle(sample)
    print(sample)
