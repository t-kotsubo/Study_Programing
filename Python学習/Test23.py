import random
# try:
#     raise TypeError("エラー発生")
# except NameError:
#     print("NameErrorエラー処理しました！")
# except ValueError:
#     print("ValueError処理しました")
# except Exception:
#     print("エラーを処理しました")
# else:
#     print("エラーが発生しませんでした")
# finally:
#     print("例外処理を終了します。")

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except B:
#         print("B")
#     except C:
#         print("C")
#     except D:
#         print("D")

# print(random.sample(range(20,25), 5))
for i in range(10):
    print(random.randrange(90,100))

