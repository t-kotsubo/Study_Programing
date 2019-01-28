import re

a = "ABCDEFGHIJ"
# b = "^ABC"
# c = "ABCD"
# d = "HIJ$"

# str = [b, c, d]

str = ["^ABC", "ABCD", "HIJ$","ABCDEFGHIJ"]

for i in str:
    if i == a:
        print(i + 'は' + a + 'と等しいです。')
    else:
        print(i + 'は' + a + 'と等しくないです。')



