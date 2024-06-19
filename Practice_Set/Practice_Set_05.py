# Write a program to create a dictionary of Hindi words with values as their English translation. 
# Provide user with an option to look it up!

dictionary = {
    "Namaste" : "Greetings",
    "Jaao" : "go",
    "Suprabhat" : "Good Morning",
    "Shubh ratri" : "Good Night"
}

print("The dictionary has the following words")
print('''
Namste
Suprabhat
Shubh Ratri
Jaao
''')
key = input("Word you want meaning of : ")

print(dictionary[key])


# Write a program to input eight numbers from the user and display all the unique numbers (once).

numbers = set()

number_one = int(input("Enter number 1 : "))
numbers.add(number_one)

number_two = int(input("Enter number 2 : "))
numbers.add(number_two)

number_three = int(input("Enter number 3 : "))
numbers.add(number_three)

number_four = int(input("Enter number 4 : "))
numbers.add(number_four)

number_five = int(input("Enter number 5 : "))
numbers.add(number_five)

number_six = int(input("Enter number 6 : "))
numbers.add(number_six)

number_seven = int(input("Enter number 7 : "))
numbers.add(number_seven)

number_eight = int(input("Enter number 8 : "))
numbers.add(number_eight)

print(numbers)
