import random

answer = random.randint(1, 100)
# answer = 70

print("--------------------------------------------------------------------")
print("                  Welcome to number guessing game!                  ")
print("--------------------------------------------------------------------")

user_input = int(input("\nEnter your guess : "))
attempts = 1

while (user_input != answer) :
    if (user_input > answer) :
        print("Try a lower number.")
    elif (user_input < answer) :
        print("Try a greater number.")
    user_input = int(input("\nEnter your guess : "))
    attempts += 1
else :
    print("\nYou guessed it right!")
    print(f"It took you {attempts} attempts to guess it right.\n")