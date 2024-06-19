# -------------- Write a python program to display a user entered name followed by Good Afternoon -------------- 

user_name = input("Enter your name : ")
print(f"Good Afternoon! {user_name}")


# -------------- Write a program to fill in a letter template given below with name and date. --------------

name = input("Enter your name : ")
date = input("Enter today's date : ")

print(f'''
Dear {name},
You are selected!
{date}
''')


# -------------- Write a program to detect double space in a string --------------

input_string = input("Enter a string : ")
result = input_string.find("  ")

print(f"This string includes double spaces at index {result}.")


# -------------- Replace the double space from problem 3 with single spaces. --------------

input_string = input("Enter a string : ")
result = input_string.replace("  ", " ")

print(f"This string includes double spaces at index {result}.")


# -------------- Write a program to format the following letter using escape sequence characters. --------------

letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
print(letter)


# ---------------------------------------------- THE END ----------------------------------------------