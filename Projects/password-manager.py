master_password = "I am god"

print("\n-------------------------------")
print("Welcome to my password manager!")
print("-------------------------------\n")

proceed = input("Do you want to access all your passwords? ").lower()


passwords = {

}

if proceed != 'yes' :
    quit()

user_pass = input("\nEnter the master password : ")

while (user_pass != master_password) :
    user_pass = input("Enter the master password : ")

while proceed == "yes" :

    user_action = None

    def show_passwords () :

        if len(passwords) > 0 :
            print("\nYour passwords are as follows : \n")

            for password in passwords :
                print(f"{password} : {passwords[password]}")

            print()

        else :
            print("\nYou have not stored any passwords here.\n")


    def add_password () :
        new_pass_key = input("By which name do you want to store this password ? ")
        new_pass = input(f"Enter the password : ")
        passwords[new_pass_key] = new_pass
        print("Successfully added a new password.")


    def remove_password () :
        for password in passwords :
                print(f"{password} : {passwords[password]}")
        print()
        remove_pass = input("Which password do you want to remove ? ").lower()

        passwords.pop(remove_pass)


    def commands () :
        print("\nWhat would you like to do ?\n")
        print("Press 1 for viewing all your passwords.")
        print("Press 2 for add a new password.")
        print("Press 3 for removing an existing password.")
        print("Press 4 to quit the program.\n")
        user_action = int(input("Enter the number of task you would like to do : "))
        if user_action == 1 :
            show_passwords()
        elif user_action == 2 :
            add_password()
        elif user_action == 3 :
            remove_password()
        elif user_action == 4 :
            global proceed
            proceed = "no"
        else :
            print("\nEnter a valid option")

    commands()