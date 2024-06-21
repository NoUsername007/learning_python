
def find_Average () :                       # Function Definition
    a = int(input("\nEnter a number : "))
    b = int(input("Enter a number : "))
    c = int(input("Enter a number : "))

    average = (a + b + c) / 3

    print(f"\nThe average of {a}, {b} and {c} is {average: .2f}.", end="\n\n")

# find_Average()                              # Function Call


def greeting () :
    username = input("\nEnter your name : ")
    print(f"\nGood day! {username}.\n")

# greeting()

def good_Day (name, ending="!") :
    print(f"Have a good day, {name}{ending}")

good_Day("Adwait")

