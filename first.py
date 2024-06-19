a = 1               # a is a number
b = 3.14            # b is a floating point number
c = True            # c is a boolean value
d = None            # d is a none type variable 
name = "Harry"      # name is a string


# -------------------- Comparison Operators -------------------

x = 7 < 2
y = 4 > 2
z = 5 == -5

print("")

print("The result is:", x, y, z)

print("")


# -------------------- LOGICAL OPERATORS ----------------------

# -------- Truth table of "OR" --------
print("True or true gives", True or True)
print("True or false gives", True or False)
print("False or true gives", False or True)
print("False or false gives", False or False)

print("\n")

# -------- Truth table of "AND" --------
print("True and true gives", True and True)
print("True and false gives", True and False)
print("False and true gives", False and True)
print("False and false gives", False and False)

print("\n")

# -------- "NOT" operator --------
print("Not of true is", not(True))
print("Not of false is", not(False))


# -------------------- How to find Datatypes --------------------

test = int("31")

print(test, type(test))


# -------------------- INPUT Function ---------------------------

input_one = int(input("Enter number 1 : "))
input_two = int(input("Enter number 2 : "))
input_three = int(input("Enter number 3 : "))

print("The 1st number is", input_one)
print("The 2nd number is", input_two)
print("The 3rd number is", input_three)

print("The sum of these numbers is ", input_one + input_two + input_three)