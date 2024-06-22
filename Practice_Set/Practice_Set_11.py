# . Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector_2D :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def details (self) :
        print(f"The vector is {self.x}i + {self.y}j.")


class Vector_3D (Vector_2D) :
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def details (self) :
        print(f"The vector is {self.x}i + {self.y}j + {self.z}k.")


example_2D_vector = Vector_2D(23, 50)
example_3D_vector = Vector_3D(23, 50, 90)

# example_2D_vector.details()
# example_3D_vector.details()


# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animal :
    def __init__(self, species):
        self.species = species

    def know_species (self) :
        print(f"The species of this animal is {self.species}.")

class Pets (Animal) :
    is_Domestic = True

    @staticmethod
    def is_Domestic () :
        print("These animals are domestic.")

class Dogs (Pets) :

    species = "dog"

    def __init__(self, breed):
        self.breed = breed

    def know_breed (self):
        print(f"The breed of this dog is {self.breed}.")

    @staticmethod
    def bark () :
        print("Bow! Bow! Bow!")

german_shepherd = Dogs("German Shepherd")
# german_shepherd.know_species()
# german_shepherd.is_Domestic()
# german_shepherd.know_breed()
# german_shepherd.bark()


# Create a class ‘Employee’ and add salary and increment properties to it.

class Employee :
    def __init__(self, salary, increment):
        self.salary = salary
        self.incremented = increment
    
    increment = 700

    def details (self) :
        print(f"The salary is {self.salary} and increment is {self.increment}.")

    @property
    def salary_after_increment (self) :
        return f"The salary after increment is {self.salary + self.salary * self.increment / 100}"
    
    @salary_after_increment.setter 
    def salary_after_increment (self, value) :
        self.increment = self.increment + 500

employee = Employee(6000, 1000)

# employee.details()


# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex :
    def __init__(self, i , r):
        self.i = i
        self.r = r

    def __add__ (self, another) :
        return f"{self.r}, {self.i} + {another.r}, {another.i} = {self.r + another.r}, {self.i + another.i}"
    
c1 = Complex(1, 2)
c2 = Complex(5, 4)

# print(c1 + c2)


# Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.

class Vector :
    def __init__(self, x, y , z):
        self.x = x
        self.y = y
        self.z = z

    def __add__ (self, another):
        return f"The resultant vector will be {self.x + another.x} {self.y + another.y} {self.z + another.z}."
    
    def __mul__ (self, another):
        return f"The dot product will be {self.x * another.x + self.y * another.y  + self.z * another.z}."
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

    def __len__ (self) :
        list = [self.x , self.y, self.z]
        return len(list)
    
    
v1 = Vector(90, 90, 90)
v2 = Vector(10, 10, 10)

print(len(v2))

# print(v1 + v2)
# print(v1 * v2)


# 