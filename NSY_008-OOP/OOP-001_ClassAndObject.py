##################################################################################################
#### Class & Object
##################################################################################################
"""
In Python, classes and objects are fundamental concepts of object-oriented programming. 
A class is like a blueprint or a template for creating objects, and an object is an instance of a class.

Class
A class defines the properties (attributes) and behaviors (methods) that its objects will have. 
For example, if you want to model a "Car," a class would define the characteristics of a car, 
like brand and color, and the actions it can perform, like drive.

Object
An object is created based on the class and represents a specific instance of that blueprint. 
For example, if "Car" is a class, objects can be instances like "Tesla" or "Maruti."

"""

print ("\n####################### OBJECT ORIENTED PROGRAMMING ################################")
print ("###################### CLASS AND OBJECT ###########################################\n")
print ("""A Class is a blueprint for creating objects. It defines the structure and behavior 
       that the object will have.
        An Object is an instance of class, representing a specific entity.

Both __init__ and self are essential parts of defining and working with classes in Python. 
Here's what they mean:
__init__
The __init__ method is a special method in Python, also known as the constructor. 
It is automatically called when you create a new object of a class. Its main purpose is to 
initialize the attributes (variables) of the object.
•	Think of __init__ as the setup or preparation method where you define and assign the initial state of the object.
•	It ensures that each object starts with the necessary attributes.

self is a reference to the current object of the class. It is used to access the 
attributes and methods of the object within the class.
•	It allows you to distinguish between instance attributes/methods (specific to the object) and local variables within the methods.
•	Think of self as a placeholder for the object that calls the method.

Class Attributes
•	Class attributes are shared across all instances of the class.
•	They are defined inside the class but outside of any methods, typically at the top of the class definition.
•	These attributes belong to the class itself, not to any specific object (instance).
•	If a class attribute is modified, the change is reflected in all instances unless overridden by an instance attribute.

Instance Attributes
•	Instance attributes are unique to each object (instance) of the class.
•	They are typically defined inside the __init__ method using self.
•	Changes to instance attributes affect only that specific object.

       """)
print ("####################################################################################\n")



print ("\n####################### Example-1 #################################################")

class Person:
    # Initialize attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    # Define a method
    def greet(self):
        print (f"Hello, my name is {self.name} and I am {self.age} years old")


# Creat an object (instance of the class)
person1 = Person("Allen", 14)
person1.greet() # Output: Hello, my name is Allen and I am 14 years old

print ("""
NOTE:
In this example, the Person class has attributes name and age, and a method greet. 
We create an object person1 using the class and call the method greet.
""")
print ("####################################################################################\n")


print ("\n####################### Example-2 #################################################")

class Rectangle:
    # Initilaizing attributes
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Defining method Area
    def area(self):
        print (f"Area of rectangle is {self.length * self.width}")

    # Defining method perimeter
    def perimeter(self):
        print (f"Perimeter of rectangle is {2 * (self.length + self.width)}") 
   
# Creating an obect rectangle1 from the class rectangle and then calling methods
# area and perimeter respectively

rectangle1 = Rectangle(4,5)
rectangle1.area()
rectangle1.perimeter()
print ("""
NOTE: 
In this example, the Rectangle class has methods area and perimeter to perform 
operations related to rectangles. 
The object rectangle1 is used to compute the area and perimeter.
""")
print ("####################################################################################\n")


print ("\n####################### Example-3 #################################################")
print ("""
NOTE: 
In this example, You will learn about Class Attributes
Class Attributes
•	Class attributes are shared across all instances of the class.
•	They are defined inside the class but outside of any methods, typically at the top of the 
    class definition.
•	These attributes belong to the class itself, not to any specific object (instance).
•	If a class attribute is modified, the change is reflected in all instances unless overridden
    by an instance attribute.
""")
print ("####################################################################################\n")
class Car:
    # Class Attribute
    wheels = 4

    # Initilizing Attributes
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
# Accessing Class attributes
print ("The class attribute wheels defined in class Car is: ", Car.wheels)

# Creating Instances
print ("Creating two instances of Car - car1 and car2")
car1 = Car("Tesla", "Red")
car2 = Car("Hyundai", "White")
print ("Accessing the Class attributes shared by the Object instances")
print (f"Wheels in car1 : {car1.wheels}")
print (f"Wheels in car2 : {car2.wheels}")

# Changing the Class attribute wheels 4 to wheels = 6
print ("Changing the Class attribute wheels = 4 to wheels = 6 \n")
Car.wheels = 6
print ("Let's check if the instance car1 and car2 instances have wheels attribute updated to 6\n")
print(f"The wheels attribute of car1 : {car1.wheels}")
print(f"The wheels attribute of car2 : {car2.wheels}")


print ("\n####################### Example-4 #################################################")
print (
"""NOTE: 
In this example, You will learn about Instance Attributes
Instance Attributes:
 Instance attributes are unique to each object (instance) of the class.
 They are typically defined inside the __init__ method using self.
 Changes to instance attributes affect only that specific object.""")
print ("####################################################################################\n")

class Car:
    
    # Class Attribute
    wheels = 4 
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Creating instances
print ("Creating two object car1 and car2: car1 = Car('Tesla', 'Red') and car2 = Car('Hyundai', 'White')\n")
car1 = Car("Tesla", "Red")
car2 = Car("Hyundai", "White")
print ("The Instance attributes are unique for each object car1 and car2")
print (f"Car1 Brand and Color is {car1.brand}, {car1.color} respectively")
print (f"Car2 Brand and Color is {car2.brand}, {car2.color} respectively")

print ("Modifying an instance attribute : car1.color = 'Black'")
car1.color = "Black"
print (f"Car1 Brand and Color is {car1.brand}, {car1.color} respectively")
print ("####################################################################################\n")


print ("\n####################### Example-5 #################################################")
print (
"""NOTE: 
In this example, You will learn What happens if an instance attribute shares the same name as 
a class attribute?
When an instance attribute shares the same name as a class attribute, 
the instance attribute takes precedence over the class attribute for that specific object. 
This means that when you access the attribute via the object, Python will look for the instance 
attribute first and use it, ignoring the class attribute.

Here’s a detailed explanation and example:

What Happens
Instance Attribute Overrules: The instance-specific value is used whenever you access the 
attribute through the object.

Class Attribute Remains Intact: The class attribute is still accessible through the class itself 
or through objects that don’t override it.""")
print ("####################################################################################\n")

class Animal:
    # Class Attribute
    species = "Mammal"

    def __init__(self, name):
        self.name = name # Instance attribute

# Creating an object
dog = Animal("Dog")

# Accessing Attributes
print (f"Name of the Species for the instance dog is : {dog.species}")

print ("Changing the species attribute of the instance dog dog.species = 'Cannine'")
dog.species = "Cannine"
print (f"Name of the species for the instance dog is : {dog.species}")
print (f"Name of the Species for the Class Animal is {Animal.species}")
print ("####################################################################################\n")


print ("\n####################### Example-6 #################################################")
print (
"""NOTE: 
In this example, How does inheritance affect class and instance attributes?
In Python, inheritance allows a child class to acquire attributes and methods from a parent class. 
It affects both class attributes and instance attributes in specific ways:

Class Attributes in Inheritance
1. Shared Across Parent and Child Classes:
    Class attributes defined in the parent class are automatically inherited by the child class.
    Both the parent and child class, as well as instances of both, can access these shared attributes.

2. Overriding Class Attributes:
    If the child class defines a class attribute with the same name as the parent class, it overrides 
    the parent’s class attribute for the child class and its instances.
    The parent class’s attribute remains unchanged.

Instance Attributes in Inheritance
Inherited Instance Attributes:
1. When creating an object of the child class, the __init__ method in the parent class can initialize 
    instance attributes, provided the child class does not override it.
2. Overriding Instance Attributes:
    The child class can define its own __init__ method, which can modify or redefine the instance 
    attributes inherited from the parent class.
""")
print ("####################################################################################\n")

class Animal:
    species = "Mammal"

class Child(Animal):
    species = "Reptile"

# Accessing class attributes
print (f"Animal species is {Animal.species}")
print (f"Child species is {Child.species}")
print ("####################################################################################\n")

print ("\n####################### Example-6 #################################################")
print (
"""NOTE: 
In this example, How does inheritance affect class and instance attributes?
In Python, inheritance allows a child class to acquire attributes and methods from a parent class. 
It affects both class attributes and instance attributes in specific ways:

Class Attributes in Inheritance
1. Shared Across Parent and Child Classes:
    Class attributes defined in the parent class are automatically inherited by the child class.
    Both the parent and child class, as well as instances of both, can access these shared attributes.

2. Overriding Class Attributes:
    If the child class defines a class attribute with the same name as the parent class, it overrides 
    the parent’s class attribute for the child class and its instances.
    The parent class’s attribute remains unchanged.

Instance Attributes in Inheritance
Inherited Instance Attributes:
1. When creating an object of the child class, the __init__ method in the parent class can initialize 
    instance attributes, provided the child class does not override it.
2. Overriding Instance Attributes:
    The child class can define its own __init__ method, which can modify or redefine the instance 
    attributes inherited from the parent class.
""")
print ("####################################################################################\n")

class Parent:
    def __init__(self, name, location):
        self.name = name # Instance attribute
        self.location = location

class Child(Parent):
    def __init__(self, name, location, age):
        super().__init__(name, location) # Inherits 'name' and location from Parent Class
        self.age = age        # Additional attribute for Child Class

print ("Creating two objects parent and child of the class Parent and class Child")
# Creating objects
parent = Parent("Alice", "Bangalore")
child = Child("Bob", "Bangalore", 10)

print(f"name attribute from parent is {parent.name}")
print(f"name attribute from child is {child.name}")
print(f"age attribute from chile is {child.age}")
print ("####################################################################################\n")





