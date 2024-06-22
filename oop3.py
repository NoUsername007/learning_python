class Employee :
    a = 1

    @classmethod
    def show (cls) :
        print(f"The class attribute of a is {cls.a}.")

    @property
    def name (self) :
        return f"Your name is {self.fname} {self.lname}."
    
    @name.setter
    def name (self, value) :
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    
e = Employee()

e.name = 'Shah rukh khan'

print(e.name)



class Number :
    def __init__(self, n):
        self.number = n

    def __add__(self, num) :
        return self.number * num.number

a = Number(1)
b = Number(2)

print(a + b)