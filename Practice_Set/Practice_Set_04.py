# --------------------- Write a program to store seven fruits in a list entered by the user ------------------------

fruits = []

first_fruit = input("Enter the first fruit : ")
fruits.append(first_fruit)

second_fruit = input("Enter the second fruit : ")
fruits.append(second_fruit)

third_fruit = input("Enter the third fruit : ")
fruits.append(third_fruit)

fourth_fruit = input("Enter the fourth fruit : ")
fruits.append(fourth_fruit)

fifth_fruit = input("Enter the fifth fruit : ")
fruits.append(fifth_fruit)

sixth_fruit = input("Enter the sixth fruit : ")
fruits.append(sixth_fruit)

seventh_fruit = input("Enter the seventh fruit : ")
fruits.append(seventh_fruit)

print(f"\nThe fruits you entered are {fruits}\n")


# ---------------- Write a program to accept marks of 6 students and display them in a sorted manner. ----------------

marks = []

student_one = int(input("Marks of student one : "))
marks.append(student_one)

student_two = int(input("Marks of student two : "))
marks.append(student_two)

student_three = int(input("Marks of student three : "))
marks.append(student_three)

student_four = int(input("Marks of student four : "))
marks.append(student_four)

student_five = int(input("Marks of student five : "))
marks.append(student_five)

student_six = int(input("Marks of student six : "))
marks.append(student_six)

marks.sort()

print(marks)


# ------------- Check that a tuple type cannot be changed in python. -------------

tuple1 = ()

tuple1[0] = 1

print(type(tuple1))
print(tuple1)                   # Shows error as tuple is immutable


# ------------- Write a program to sum a list with 4 numbers. -------------

sum_list = [2, 4, 8, 16, 500, 1500]

sum = sum(sum_list)               # Calculates the sum of all elements of a list

print(sum)


# ------------- Write a program to count the number of zeros in the following tuple -------------

a = (7, 0, 8, 0, 0, 9)

count_of_zero = a.count(0)          # Counts the number of zeros in the list

print(count_of_zero)


# ---------------------------------------------- THE END ----------------------------------------------