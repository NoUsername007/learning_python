print("\nWelcome to my computer quiz!")

boolean = input("\nDo you want to play? ").lower()

if boolean != "yes" and boolean != "yeah" :
    quit()

user_score = 0

print("\nQuestion 1 : What is the full form of RAM?")
input_1 = input("Answer : ").lower()
answer_1 = "random access memory"

if input_1 == answer_1 :
    user_score += 1

print()

print("Question 2 : What is the full form of ROM?")
input_2 = input("Answer : ").lower()
answer_2 = "read only memory"

if input_2 == answer_2 :
    user_score += 1

print()

print("Question 3 : What is the full form of BIOS?")
input_3 = input("Answer : ").lower()
answer_3 = "basic input output system"

if input_3 == answer_3 :
    user_score += 1

print()

print("Question 4 : What is the full form of CS?")
input_4 = input("Answer : ").lower()
answer_4 = "computer science"

if input_4 == answer_4 :
    user_score += 1

print()

print("Question 5 : What is the full form of HDD?")
input_5 = input("Answer : ").lower()
answer_5 = "hard disk drive"

if input_5 == answer_5 :
    user_score += 1

print()

print(f"You answered {user_score} questions right.")
print(f"Your score is  {user_score} out of 5.")

print()