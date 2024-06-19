i = 0

names = ["Adwait", "Akshad", "Arnav", "Atharva", "Manas", "Eashan"] 

while (i < len(names)) :
    print(names[i])
    i += 1
else:
    print("\nWhile loop done.\n")


for name in names :
    print(name)
else : 
    print("\nFor loop done.\n")


for i in range(1, 11) :
    if (i % 2 == 0) :
        continue
    print(i)

for i in range(0, 4) :
    print("Printing")
    if (i == 2) :
        continue
    print(i)
    # pass
