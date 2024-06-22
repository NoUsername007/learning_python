class Details :

    def get_info (self) :
        print(f'''Your name is {self.name}.
Your age is {self.age}.
You are a {self.gender}.''')

    def __init__(self, name , age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def static () :
        print("\nGreetings!")

    def print_name (self) :
        print(self.name)

adwait = Details("Adwait", 15, "Male")

akshad = Details("Akshad", 16, "male")

atharva = Details("atharva", 14, "female")

adwait.get_info()
adwait.static()
adwait.print_name()

print("\n\n\n")

akshad.get_info()
akshad.static()
akshad.print_name()

print("\n\n\n")

atharva.get_info()
atharva.static()
atharva.print_name()

# print(adwait.name, adwait.age, adwait.gender)
# print(akshad.name, akshad.age, akshad.gender)
# print(atharva.name, atharva.age, atharva.gender)

# Class attributes are attributes which belong to the class
# Object attributes belong only to the object