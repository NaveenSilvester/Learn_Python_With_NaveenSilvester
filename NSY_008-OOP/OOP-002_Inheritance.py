##################################################################################################
#### Inheritance Property in Object Oriented Programming
##################################################################################################
"""
Inheritance is one of the key concepts in Object-Oriented Programming (OOP). It allows one class 
(called the child class or subclass) to inherit properties (attributes) and methods from another 
class (called the parent class or superclass). This promotes code reuse and enables developers to 
build upon existing functionality.
"""

print ("\n####################### Example-1 #################################################")
print ("""
We have created two classes Parent and Child. The Child Class inherits from the Parent Class both 
attributes (name and location) as well as methods (display). The Child Class also has its own
attribute named "age". The Child class can override the Parent attributes name and location.
The child Class has its own method named "get_age".
Note: While Creating the Child Class you will have to mention the Name of the Class to be inherited
Ex. class Child(Parent):
To Inherit the attributes from Parent Class, you need to initiate it by 
super().__init__(self, attributes from Parent)
""")
# Parent Class (Super Class)

class Parent:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    

    def display(self):
        return (f"{self.name}, Location: {self.location}")

    def greet(self):
        return (f"Hello {self.name} from Parent Class")

class Child(Parent):
    def __init__(self, name, location, age):
        super().__init__(name, location)
        self.age = age
    
    def get_age(self):
        return (f"{self.name}, {self.age} and {self.location}")

    def greet(self):
        return (f"Hello {self.name} from Child Class")
    

parent = Parent("Raj", "Bangalore")
child  = Child("Shoba", "Mysore", 20)

print (f"Here are the details of the parent object : {parent.display()}:")
print (f"Here are the details of the child object : {child.get_age()}:")
print (f"{parent.greet()}")
print (f"{child.greet()}, Child Class Overrides Parent Class Attributes")

print("##################################################################################\n")

print ("\n####################### Example-2 #################################################")
# Parent Class: Vehicle
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels
    
    def display_details(self):
        print (f"Brand : {self.brand}, Wheels : {self.wheels}")


class Car (Vehicle):
    def __init__(self, brand, wheels, fuel_type):
        super().__init__(brand, wheels) # Inherit 'brand' and 'wheels'
        self.fuel_type = fuel_type  # Car-specific attribute

    def display_fuel_type(self):
        print(f"Fuel Type: {self.fuel_type}")

class Bike (Vehicle):
    def __init__(self, brand, wheels, has_gear):
        super().__init__(brand, wheels)
        self.has_gear = has_gear
    
    def display_gear_info(self):
        print(f"Has Gear : {'Yes' if self.has_gear else 'No'}")

# Create Objects
car = Car("Tesla", 4, "Electric")
bike = Bike("BMW", 2, True)
car.display_fuel_type()
bike.display_gear_info()
print("##################################################################################\n")


class first:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def greet(self):
        print(f"Name is {self.name}, Location is {self.location}\n")


class second(first):
    def __init__(self, name, location, age):
        super().__init__(name,location)
        self.name = name
        self.location = location
        self.age = age
    
    def greet(self):
        print(f"Name from second {self.name}, Location {self.location}, Age {self.age}\n")


First = first("Naveen", "Bangalore")
Second = second("Allen", "Bangalore", 15)
First.greet()