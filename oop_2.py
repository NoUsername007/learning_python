class Employee :
    company = "ITC"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info (self) :
        print(f"The employee's name is {self.name}.")
        print(f"His salary is {self.salary}.")


class Programmer (Employee) :
    company = "ITC Infotech"

    language = "Python"

    @classmethod
    def lang_info (cls) :
        print(f"He is good at {cls.language} programming language.")


class Coder(Programmer) :
    def hello_world (self) :
        print("Hello, World !")

employee_one = Employee("NoUsername", "900k")
programmer_one = Programmer("Adwait", "1M")
coder_one = Coder("Adwait", "500k")

# print(employee_one.company)
# employee_one.info()

print()

# coder_one.hello_world()
programmer_one.info()
programmer_one.lang_info()