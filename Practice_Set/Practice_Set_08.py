# Write a program using functions to find greatest of three numbers.

def find_greatest_number () :
    number = int(input("\nEnter the number of numbers : "))
    print()
    list = []
    for i in range(1, number + 1) :
        a = int(input("Enter the number : "))
        list.append(a)
    return f"\nThe greatest number is {max(list)}.\n"

# print(find_greatest_number())


# Write a python program using function to convert Celsius to Fahrenheit.

def convert_temperature() :
    user_input = int(input("Enter the temperature : "))
    unit = input("Enter the unit ( F or C ) : ")

    unit = unit.upper()

    if (unit == "C") :
        return f"The temperature is {((user_input * 9/5 + 32)): .2f} °F ."
    if (unit == "F") :
        return f"The temperature is {( (user_input - 32) * (5/9)) : .2f} °C ."
    
# print(convert_temperature())


# Write a recursive function to calculate the sum of first n natural numbers.

def recursive_sum (n) :
    if (n == 0) :
        return 0
    
    return n + recursive_sum(n - 1)

# print(recursive_sum(11))


# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def pattern (n) :
    for i in range(0, n+1) :
        print("*" * (n - i))

# pattern(5)


# Write a python function which converts inches to cms

# def convert_inches_to_cm () :
#     user_input = int(input("Enter length in inches : "))
#     return (user_input * 2.54)

# print(f"The length is {convert_inches_to_cm()} in cm.")


# Write a python function to remove a given word from a list ad strip it at the same time.

le = ["mango", "apple", "banana", "watermelon", "grapes"]

def remove_word (l) :
    user_input = input("Enter the word : ")
    n= []

    for item in l :
        
        if not (item == user_input) :
            n.append(item.strip(user_input))
        
    return n

# print(remove_word(le))

# for items in list :
#     print(items)


# Write a python function to print multiplication table of a given number.

def table (n) :
    for i in range (1, 11) :
        print(f"{n} x {i} = {n * i}")

table(10)