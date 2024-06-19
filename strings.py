# Strings can be defined using '' or "" or ''' or """"

single_quotes = 'Harry'
double_quotes = "Harry"
triple_single_quotes = '''Harry Bhai!'''
triple_double_quotes = """Harry Bhai!"""

name = single_quotes[0 : 3]               # Starting index is included the finishing index is not.
last_character = single_quotes[-1]        # Negative indices are counted from the end of the string. It does not include zero.

print(name + "ish")
print(last_character)


# ----------------------------- String Functions -----------------------------

name = "NoUsername007"

print(len(name))                        # Used to find the length of a string
print(name.startswith("No"))            # Used to find if the string starts with the given arguement return true or false
print(name.endswith("007"))             # Used to find if the string ends with the given arguement return true or false
print(name.capitalize())                # Capitalizes the first character of the string
print(name.upper())                     # Capitalizes all the character of a string
print(name.lower())                     # Converts all the characters of a string to lowercase
print(name.title())                     # Capitalizes first letter of each word
print(name.rstrip())                    # All the leading and trailing white spaces of the string are removed
print(name.count("n"))                  # Counts the total number of occurrences of any character
print(name.find("Username"))            # Finds a word and returns the index of first occurrence of that word in the string.
print(name.replace("007", "009"))       # Replaces the old word with new word in the entire string.


# ----------------------------- String Functions -----------------------------

print("First line,\nNext line")           # Prints a new line
print("This is a \tTab space")            # Prints a tab space
print("Hello, \"World\"!")                # Makes the subsequent character a string