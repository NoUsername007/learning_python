# In dictionary the data is stored in key value pairs

marks = {
    "Adwait" : 95,
    "Akshad" : 96,
    "Arnav" : 94,
    "Atharva" : 89 
}

# print(marks["Atharva"])


# Dictionary methods

# print(marks.items())              # Prints the items of a dictionary
# print(marks.keys())               # Prints the keys of a dictionary
# print(marks.values())             # Prints the value of a dictionary

# marks.update({"Atharva" : 90})    # Updates the dictionary

# print(marks["Atharva"])

# print(marks.get("Ash"))           # .get method will not return error even if there is not key of the passed arguement. Sqaure bracket does give error if the key passed is not present.


# Sets 

empty_set = set()                   # Create an empty set using set() as {} will create an empty dictionary
set = { 1, 2, 35, 6, 7, -1 }        
set.add(69)                         # Adds a specified elements to the set
set.remove(35)                      # Removes the specified element in the set

print(set)
print(len(set))

set2 = {2, 69, 70, 71}

print(set.intersection(set2))