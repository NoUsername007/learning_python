import math
import random
    
    
    # -------------------------------------------------------------------------------------------------------------
    # This is the lenghth version of the same code below but is more readable                                            
    # -------------------------------------------------------------------------------------------------------------

def game () :
    user_input = input("\nChoose an input (Snake Water Gun): ")
    user_move = None
    computer_move = random.randint(1, 3)
    computer_move_name = None 

    user_input = user_input.lower()

    if (user_input == "snake") :
        user_move = 1
    elif (user_input == "water") :
        user_move = 2
    elif (user_input == "gun") :
        user_move = 3
    
    if computer_move == 1 :
        computer_move_name = "snake"
    elif computer_move == 2 :
        computer_move_name = "water"
    elif computer_move == 3 :
        computer_move_name = "gun"
    
    print(f'''
You chose {user_input}.
Computer chose {computer_move_name}.
''')
    
    
    if (user_move == computer_move) : 
        print("This is a draw.\n")
    elif computer_move - user_move == 1 or computer_move - user_move == -2 :
        print("You win!\n")
    else :
        print("You lose!\n")

game()


    # -------------------------------------------------------------------------------------------------------------
    # This is the minified version of this code working of computer_move - user_move == 1 or -2 when you lose logic
    # -------------------------------------------------------------------------------------------------------------


def game_improved () :
    user_input = input("\nChoose an input (Snake Water Gun): ")
    user_move = None
    computer_move = random.randint(1, 3)
    computer_move_name = None 

    user_input = user_input.lower()

    if (user_input == "snake") :
        user_move = 1
    elif (user_input == "water") :
        user_move = 2
    elif (user_input == "gun") :
        user_move = 3
    
    if computer_move == 1 :
        computer_move_name = "snake"
    elif computer_move == 2 :
        computer_move_name = "water"
    elif computer_move == 3 :
        computer_move_name = "gun"
    
    print(f'''
You chose {user_input}.
Computer chose {computer_move_name}.
''')

    if (user_move == computer_move) : 
        print("This is a draw.\n")
    elif computer_move - user_move == 1 or computer_move - user_move == -2 :
        print("You win!\n")
    else :
        print("You lose!\n")

game_improved()