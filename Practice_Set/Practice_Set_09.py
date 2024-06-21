# . Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

def find_twinke () :
    with open("./Practice_Set/files/poems.txt", "r") as file :
        content = file.read()
        content = content.lower()
    
    if ("twinkle" in content) :
        return "This file includes the word Twinkle."
    else : 
        return "This file does not includes the word Twinkle."
        
# print(find_twinke())


# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() 
# function breaks the Hi-score.

def updateScore (score) :
    with open("./Practice_Set/files/score.txt") as file :
        content = file.readlines()
        prev_score = int(content[-1])

    if (score > prev_score) :
        with open("./Practice_Set/score.txt", "a") as file :
            file.write(f"\nHigh Score : {score}")
        

# updateScore(100)


# Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

def tables () :
    table = ""
    for i in range(2, 21) :
        table = ""
        for j in range (1, 11) :
            table += f"{i} x {j} = {i * j}\n"
        with open(f"./Practice_Set/files/tables/{i}.txt", "w") as file :
            file.write(table)

# tables()


# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 

def donkey () :
    with open("./Practice_Set/files/donkey.txt") as file :
        content = file.read()
        content = content.lower().replace("donkey","#####")
    with open("./Practice_Set/files/donkey.txt", "w") as file :
        file.write(content)

# donkey()


# Repeat program 4 for a list of such words to be censored

def censor () :

    list = ["donkey", "monkey", "dog"]

    with open("./Practice_Set/files/donkey.txt") as file :
        content = file.read()
        for item in list :
            content = content.lower().replace(item,"#" * (len(item)))

    with open("./Practice_Set/files/donkey.txt", "w") as file :
        file.write(content)

# censor()


# Write a program to mine a log file and find out whether it contains ‘python’.

def look_for_python () :
    with open("./Practice_Set/files/python.txt") as file :
        content = file.read()
        content = content.lower()
    
    if ("python" in content) :
        return "This file includes the word python."
    else :
        return "This file does not include the word python."
    
# print(look_for_python())


# Write a program to find out the line number where python is present from ques 6.

def look_for_python_line () :
    with open("./Practice_Set/files/python.txt") as file :
        content = file.readlines()
    
    for line in content :
        if ("python" in line) :
            result = f"This file includes the word python at line number {content.index(line) + 1}."
            return result
        
# print(look_for_python_line())


# Write a program to make a copy of a text file “this. txt”

def copy () :
    with open("./Practice_Set/files/this.txt") as file :
        content = file.read()
    with open("./Practice_Set/files/this(copy).txt", "a") as file :
        file.write(content)

# copy()


# Write a program to find out whether a file is identical & matches the content of another file.

def is_identical () :
    with open("./Practice_Set/files/this.txt") as file :
        this_content = file.read()
    with open("./Practice_Set/files/this(copy).txt") as file :
        copy_content = file.read()

    if (this_content == copy_content) :
        return "The file this.txt is identical to this(copy.txt)"
    else :
        return "The file this.txt is not identical to this(copy.txt)"
    
# print(is_identical())


# Write a program to wipe out the content of a file using python.

def remove_content () :
    with open("./Practice_Set/files/this(copy).txt", "w") as file :
        file.write("")

# remove_content()


# Write a python program to rename a file to “renamed_by_ python.txt.

import os

def rename_file (name, path) :
    os.rename(name, path)

# ------------------------------------------ OR ------------------------------------------

def dupe_and_del () :
    with open("./Practice_Set/files/this_copy.txt") as file :
        content = file.read()
    with open("./Practice_Set/files/this_copy_2.txt", "w") as file :
        file.write(content)
    os.remove("./Practice_Set/files/this_copy.txt")

# rename_file("./Practice_Set/files/this(copy).txt", "./Practice_Set/files/this_copy.txt")
# dupe_and_del()