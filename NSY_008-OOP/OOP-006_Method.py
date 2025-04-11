##################################################################################################
#### Different Class methods in Python
##################################################################################################
"""
In Python, classes can define different types of methods to manipulate or access data, depending 
on their use case. These methods include instance methods, class methods, static methods, and magic 
methods.

Instance Method
Instance methods are the most common methods in Python. They take self as their first parameter, 
which refers to the instance of the class calling the method. Instance methods can access and modify 
instance attributes and invoke other instance methods.

class Example:
    def __init__(self, name):
        self.name = name
    def greet(self):  # Instance method
        return f"Hello, {self.name}!"
obj = Example("Alice")
print(obj.greet())  # Output: Hello, Alice!
Class Method
	Class methods take cls as their first parameter, which refers to the class itself (rather than the instance). 
    They are defined using the @classmethod decorator. Class methods can access class-level attributes and modify them.
class Example:
    count = 0  # Class attribute
    @classmethod
    def increment_count(cls):  # Class method
        cls.count += 1
        return cls.count
print(Example.increment_count())  # Output: 1


Static Method
	Static methods do not take any implicit first parameter like self or cls. They behave like regular 
    functions within the context of a class. Static methods are defined using the @staticmethod decorator.
     They cannot modify or access class or instance attributes directly.
class Example:
    @staticmethod
    def add(a, b):  # Static method
        return a + b
print(Example.add(5, 3))  # Output: 8


Magic Methods (Dunder Methods)
Magic methods, also known as dunder methods (short for "double underscore"), are special methods 
in Python with predefined behavior. They are usually used to define operator overloading, object 
representation, and other features.
Common Magic Methods:
•	__init__: Initializes instance attributes.
•	__str__: Represents the object as a string.
•	__add__: Implements addition operator.
•	__len__: Returns the length of the object.

"""
print ("############################################################################################")
print ("######################### Instance Method #################################################")
print ("""NOTES:
Instance methods are the most common methods in Python. They take self as their first parameter, 
       which refers to the instance of the class calling the method. Instance methods can access 
       and modify instance attributes and invoke other instance methods.
""")
print ("############################################################################################")
print("Code Output:\n")
class Example:
    def __init__(self, name):
        self.name = name
    def greet(self):  # Instance method
        return f"Hello, {self.name}!"
obj = Example("Alice")
print(obj.greet())  # Output: Hello, Alice!
print ("############################################################################################\n")

print ("############################################################################################")
print ("########################### Class Method #################################################")
print ("""NOTES:
Class methods take cls as their first parameter, which refers to the class itself 
(rather than the instance). They are defined using the @classmethod decorator. Class methods 
can access class-level attributes and modify them.
Class methods in Python are used to define functionality that applies to the class itself rather
 than to individual instances. Class methods operate on class-level attributes and are often used 
for factory methods or to handle class-level configurations. They are defined using the @classmethod 
decorator and take cls as their first parameter, which represents the class.       
""")
print ("############################################################################################")
print("Code Output:\n")
class Example:
    count = 0  # Class attribute
    @classmethod
    def increment_count(cls):  # Class method
        cls.count += 1
        return cls.count
example = Example()
print(example.increment_count())
print ("############################################################################################\n")

print ("############################################################################################")
print ("############################ Static Method #################################################")
print ("""NOTES:
Static methods do not take any implicit first parameter like self or cls. They behave like regular
 functions within the context of a class. Static methods are defined using the @staticmethod 
decorator. They cannot modify or access class or instance attributes directly.       
""")
print ("############################################################################################")
print("Code Output:\n")
class Example:
    @staticmethod
    def add(a, b):  # Static method
        return a + b
print(Example.add(5, 3))  # Output: 8
print ("############################################################################################\n")


print ("############################################################################################")
print ("############################ Static Method #################################################")
print ("""NOTES:
Real-World Example: Utility Methods in an E-Commerce Application
Imagine an e-commerce app where a class handles items in the inventory, and you need a method to 
calculate tax on an item. The tax calculation doesn't depend on the instance or class attributes, 
so a static method is perfect.  

Explanation of the Example:
Static Method (calculate_tax):
This method calculates tax based on the price and tax rate.
It does not rely on any instance-specific data (self) or class-level data (cls), making it a static 
method.

Logical Grouping:
While the calculate_tax function could exist outside the Item class, it is logically grouped within 
the class because it's related to item operations.    
""")
print ("############################################################################################")
print("Code Output:\n")
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def calculate_tax(price, tax_rate):
        return price * tax_rate

# Create an instance of Item
item1 = Item("Laptop", 50000)

# Call the static method
tax = Item.calculate_tax(item1.price, 0.18)
print(f"The tax on {item1.name} is: ₹{tax}")

print(item1.calculate_tax(item1.price, 0.18))
print ("############################################################################################")


print ("############################################################################################")
print ("############################################################################################")
print (" Testing Knowledge and Playing with Concepts of OOPs")
class Engine:
    def __init__(self):
        self.start = "Engine Started"

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def display(self):
        return (self.engine.start)

car = Car()
print (car.display())


class Parent:
    def __init__(self, Father, Mother):
        self.father = Father
        self.mother = Mother

class Child(Parent):
    def __init__(self, Father, Mother, Kid):
        super().__init__(Father, Mother)
        self.kid = Kid

    def display_family(self):
        return (f"Family Members are :\n Father: {self.father}, Mother: {self.mother}, Kid : {self.kid}")
    
kid = Child("Raj", "Rani", "Yuv")
print (kid.display_family())


class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def area(self):
        return (f"Area of Rectangle: {self.length * self.width}")
    def perimeter(self):
        return (f"Perimeter of Rectangle: {2 * (self.length + self.width)}")

class Circle:
    def __init__(self, Radius):
        self.radius = Radius
    
    def area(self):
        return (f"Area of Circle: {3.14 * self.radius ** 2}")

shapes = [Rectangle(5,3), Circle(4)]




class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received: {message}")

subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("State has changed!")
