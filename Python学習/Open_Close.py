# f = open("Sample.txt", "a")

# f.write("Hello!\n")
# f.write("Good Bye!\n")

# f.close()

with open("Sample2.txt", "r") as f:
    lines = f.readlines()

for line in lines:    
    print(line, end="")





