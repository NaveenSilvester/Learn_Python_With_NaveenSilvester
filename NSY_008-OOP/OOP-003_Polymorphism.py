##################################################################################################
#### Polymorphism Property in Object Oriented Programming
##################################################################################################
"""
Polymorphism is one of the fundamental concepts in Object-Oriented Programming (OOP). It allows 
objects of different classes to be treated as objects of a common superclass. In Python, 
polymorphism refers to the ability of different objects to be used interchangeably, typically by 
having methods with the same name but behaving differently depending on the object's class.
"""

print ("\n####################### Example-1 #################################################")
print ("""
Polymorphism is one of the fundamental concepts in Object-Oriented Programming (OOP). It allows 
objects of different classes to be treated as objects of a common superclass. In Python, 
polymorphism refers to the ability of different objects to be used interchangeably, typically by 
having methods with the same name but behaving differently depending on the object's class.

In this example:
Both Dog and Cat override the sound method of the Animal class.
When the sound method is called on an object, it executes the version specific to the 
object's class.
""")
class Animal:
    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")

# Demonstrating polymorphism
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()
print ("####################################################################################\n")

print ("\n####################### Example-2 #################################################")
print ("""
Polymorphism allows different classes to have methods with the same name and functionality,
 enabling the use of a common interface.

In this example:
    Both Rectangle and Circle have an area method, even though they belong to different classes.
    The same interface (area) is used to compute areas, regardless of the type of shape.
""")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Demonstrating polymorphism
shapes = [Rectangle(5, 4), Circle(3)]
for shape in shapes:
    print("Area:", shape.area())
print ("####################################################################################\n")


print ("\n####################### Example-3 #################################################")
print ("""
Duck Typing
 Python is dynamically typed, so it relies on "Duck Typing." If an object has the required 
 method, it can be treated as valid for polymorphism, regardless of its class.

In this example:
 The fly method is implemented in both Bird and Airplane classes.
 The perform_fly function calls the fly method without worrying about the object's type, 
 as long as it has the method.
""")

class Bird:
    def fly(self):
        print("Bird is flying!")

class Airplane:
    def fly(self):
        print("Airplane is flying!")

def perform_fly(obj):
    obj.fly()

# Demostrating Polymorphism with duck typing
perform_fly(Bird()) 
perform_fly(Airplane())
print ("####################################################################################\n")


print ("\n####################### Example-4 #################################################")
print ("""
Real-World Example: Payment System
Imagine building a payment system that supports different types of payments 
(credit card, PayPal, cryptocurrency).
""")

class Payment:
    def pay(self, amount):
        print(f"Paying {amount}")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paying CreditCard {amount}")

class DebitCard(Payment):
    def pay(self, amount):
        print(f"Paying DebitCard {amount}")

# Polymorphism in Action
def make_payment(payment_type,amount):
    print(payment_type.pay(amount))

payments = [CreditCard(), DebitCard() ]
print ("$$$$$$$$$$")
for payment_type in payments:
    amount = 10
    make_payment(payment_type, amount)
print ("####################################################################################\n")


from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass  # Abstract method

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing {amount} via Credit Card."

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing {amount} via PayPal."

# Using abstraction
payments = [CreditCardPayment(), PayPalPayment()]
for payment in payments:
    print(payment.process_payment(1000))


print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
class Payment:
    def pay(self, amount):
        print(f"Paying {amount}")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paying CreditCard {amount}")

class DebitCard(Payment):
    def pay(self, amount):
        print(f"Paying DebitCard {amount}")

# Polymorphism in Action
def make_payment(payment_type,amount):
    print(payment_type.pay(amount))

payments = [Payment(),CreditCard(), DebitCard() ]
print ("$$$$$$$$$$")
for payment_type in payments:
    amount = 10
    make_payment(payment_type, amount)
print ("####################################################################################\n")



