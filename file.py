# f = open("example.txt")

# print(f.read())

# f.close()

# The same can be written using with statement

with open("example.txt", "a") as file :
    file.write("\n...")
