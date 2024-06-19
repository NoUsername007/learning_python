# Write a program to print multiplication table of a given number using for loop.

for i in range(1, 11) :
    print(f"5 x {i} = {5 * i}")


# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l :
    if (i[0] == "S" or i[0] == "s") :
        print(f"Hello {i}!")
    else :
        continue


# Attempt problem 1 using while loop.

i = 1

while ( i < 11) :
    print(f"5 x {i} = {5 * i}")
    i += 1


# Write a program to find whether a given number is prime or not.

number = int(input("Enter a number : "))

for i in range(2, number - 1) :
    if (number % i == 0) :
        print("Number is not prime.")
        break
else :
    print("Number is prime.")


# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a number : "))
sum = 0

for i in range(1, n+1) :
    sum += i
else : 
    print(f"The sum of first {n} natural numbers is {sum}.")


# Write a program to calculate the factorial of a given number using for loop

n = input("Enter the number : ")
product = 1

for i in range(1, n + 1) :
    product *= i
else : 
    print(f"The factorial of {n} is {product}.")


# Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3

n = int(input("Enter a number : "))

for i in range (1, n + 1) :
    print(" "* (n - i), end="")
    print("*"* (2 * i - 1), end="")
    print()


# Write a program to print the following star pattern:
# *
# **
# *** for n = 3

n = int(input("Enter a number : "))

for i in range(1, n+1) :
    print("*" * i)


# Write a program to print the following star pattern.
# * * *  
# *   *  for n = 3
# * * *

n = int(input("Enter a number : "))

for i in range(1 , n+1) :
    if (i == 1 or i == n) :
        print("* " * n)
    else :
        print("*", end="")
        print(" "*(2*n - 3), end="")
        print("*", end="")
        print()


# Write a program to print multiplication table of n using for loops in reversed order

n = int(input("Enter a number : "))

for i in range(0, 10) :
    print(f"{n} x {10-i} = {(10-i)*n}")

n = int(input("Enter a number : "))

for i in range(0, n) :
    print(" " * (n - i - 1), end ="")
    print("*" * (2*i + 1))
