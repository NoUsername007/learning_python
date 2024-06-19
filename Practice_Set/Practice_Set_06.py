# Write a program to find the greatest of four numbers entered by the user.

import math

numbers = []

a = int( input("Enter a number : ") )
numbers.append(a)

b = int( input("Enter a number : ") )
numbers.append(b)

c = int( input("Enter a number : ") )
numbers.append(c)

d = int( input("Enter a number : ") )
numbers.append(d)

print(f"\nThe greatest number is {max(numbers)}.\n")


# Write a program to find out whether a student has passed or failed 
# if it requires a total of 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take marks as an input from the user.

x = int(input("\nMarks in subject 1 : "))
y = int(input("Marks in subject 2 : "))
z = int(input("Marks in subject 3 : "))

if ((x + y + z)/ 3 >= 40 and (x / 100 >= 33) and (y / 100 >= 33) and (z / 100 >= 13)) :
    print(f"\nYou have passed with{(x + y + z) / 3 : .2f}%.\n")
else : 
    print(f"\nYou have failed with{(x + y + z) / 3 : .2f}%.\n")


# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams

comment = "BUY NOW"
comment_lower = comment.lower()

if (("make a lot of money" in comment_lower) or ("buy now" in comment_lower) or ("subcribe this" in comment_lower) or ("click this" in comment_lower)) :
    print("\nThis is spam.\n")
else :
    print("\nThis is not spam.\n")


# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your username : ")

if (len(username) < 10) :
    print("Username contains less than 10 characters.")
elif (len(username) == 10) :
    print("Username contains 10 characters.")
else :
    print("Username contains more than 10 characters.")


# Write a program which finds out whether a given name is present in a list or not.

students = ["adwait", "akshad", "arnav", "atharva", "nisarg", "saksham", "rajveer", "manas", "eashan", "kaivalya"]

user_input = input("Enter your name : ")

user_input_lower = user_input.lower()

if (user_input_lower in students) :
    print(f"Your name is present in the list.")
else :
    print(f"Your name is not present in the list.")


# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("\nEnter your marks : "))
grade = None

if (100 <= marks or marks >= 90) :
    grade = "Excellent"
elif (marks >= 80) : 
    grade = "A"
elif (marks >= 70) :
    grade = "B"
elif (marks >= 60) :
    grade = "C"
elif (marks >= 50) :
    grade = "D"
elif (marks < 50 and marks >= 0) : 
    grade = "F"
else : 
    print("\nEnter valid marks.\n")

print(f"\nYour grade is {grade}.\n")


# Write a program to find out whether a given post is talking about “Harry” or not

post = input("\nEnter the post : ")

keyword = "Harry"

post.lower()

if (keyword.lower() in post) :
    print(f"\nThis post is talking about {keyword}.\n")
else :
    print(f"\nThis post is not talking about {keyword}.\n")