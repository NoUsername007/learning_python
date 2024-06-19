# ------------------------------ Lists and Tuples ------------------------------

# Lists and tuples are used to store multiple elements or objects
# Lists are mutable
# tuples are immutable

friends = ["apple", "orange", 5 , 345.6, False, "Akash", "Rohan"]

print(friends[-3])

friends[0] = "grapes"

print(friends[0])

print(friends[0:4])


# ------------------------------ List Methods ------------------------------

l1 = [2, 64, 8, 32, 16, 4]

l1.append(128)                      # Adds an element to the end of the list
l1.sort()                           # Sorts the list in ascending order
l1.reverse()                        # Reverses the current string
l1.insert(0, 256)                   # Inserts an element at the specified index
print(l1.pop(4))                    # Deletes the element at the specified index (if index is not specified last element is deleted) and returns the deletd value
l1.remove(32)                       # Removes the element from the list

print(l1)


# ------------------------------ Tuple ------------------------------

tuple1 = (1,3,5,7,7,7,7,) 

print(type(tuple1))


# ------------------------------ Tuple Methods ------------------------------

count_of_7 = tuple1.count(7)        # Returns the count of the number 

index_of_5 = tuple1.index(5)        # Returns the first index of the specified number