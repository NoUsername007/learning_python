# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer :
    def __init__(self, name, post, salary, age):
        self.name = name
        self.post = post
        self.salary = salary
        self.age = age

    def get_info (self) :
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Post   : {self.post}")
        print(f"Salary : {self.salary}")

adwait = Programmer("Adwait", "CEO", "40 Cr", 15)
kabir = Programmer("Kabir", "Senior Dev", "10 Cr", 16)

# adwait.get_info()

# print("\n")

# kabir.get_info()


# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator :
    def __init__(self, number):
        self.number = int(number)
    
    def square (self) :
        print(f"The square of {self.number} is {pow(self.number, 2)}.")
    
    def cube (self) :
        print(f"The cube of {self.number} is {pow(self.number, 3)}.")
    
    def sqrt (self) :
        print(f"The square root of {self.number} is {pow(self.number, 1/2) : .2f}.")

# test = Calculator(3)

# test.square()
# test.cube()
# test.sqrt()


# Add a static method in problem 2, to greet the user with hello.

class Calculator_copy :

    @staticmethod
    def hello () :
        print("Hello ! \n")

    def __init__(self, number):
        self.number = int(number)
    
    def square (self) :
        print(f"The square of {self.number} is {pow(self.number, 2)}.")
    
    def cube (self) :
        print(f"The cube of {self.number} is {pow(self.number, 3)}.")
    
    def sqrt (self) :
        print(f"The square root of {self.number} is {pow(self.number, 1/2) : .2f}.")

# test = Calculator_copy(3)
# test.hello()
# test.square()
# test.cube()
# test.sqrt()


# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and 
# get fare information of train running under Indian Railways.

class Train :
    def book_ticket (self) :
        print("Your ticket is booked.")

    def get_status (self) :
        print("There are currently no seats available.")
    
    def get_fare_info (self) :
        print("The fare info can be seen on the Indian railways website.")

test = Train()

test.book_ticket()
test.get_status()
test.get_fare_info()