# ------------ Write a program to print Twinkle twinkle little star poem in python. ------------

print('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.''')


# -------------- Install an external module and use it to perform an operation of your interest. ------------

import pyjokes

print(pyjokes.get_joke())


# -------------------------------- Use REPL and print the table of 5 using it. -----------------------------

print(5 * 1)
print(5 * 2)
print(5 * 3)
print(5 * 4)
print(5 * 5)
print(5 * 6)
print(5 * 7)
print(5 * 8)
print(5 * 9)
print(5 * 10)


# ------------ Write a python program to print the contents of a directory using the os module. ------------
# --------------------------- Search online for the function which does that. ------------------------------
# ------------------------- Label the program written in problem 4 with comments. --------------------------

import os

def print_directory_contents(path):
    try:
        # List the contents of the directory
        directory_contents = os.listdir(path)
        
        print(f"Contents of '{path}':")
        for item in directory_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = '.'  # Current directory
print_directory_contents(directory_path)


# ---------------------------------------------- THE END ----------------------------------------------