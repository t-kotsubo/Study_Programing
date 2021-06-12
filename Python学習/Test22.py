import re

# raw文字列
# print("\n")
# print("\\n")
# print(r"\n")

# print(re.match(r'[0-9]{7}', '12345678'))
# print(re.fullmatch(r'[0-9]{7}', '12345678'))

# 正規表現を使って文字列のパターンがマッチするか確認
print(re.fullmatch(r'[0-9]{3}-[0-9]{4}', '123-4567'))
print(re.fullmatch(r'[0-9]{3}-[0-9]{4}', '1234-567'))
# 実行結果：
# <re.Match object; span=(0, 8), match='123あ4567'>
# None


