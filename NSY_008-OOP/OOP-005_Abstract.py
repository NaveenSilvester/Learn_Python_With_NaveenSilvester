##################################################################################################
#### Abstraction in Object Oriented Programming
##################################################################################################
"""
Abstraction is an object-oriented programming (OOP) concept that focuses on hiding the 
implementation details of an object and exposing only the essential features to the user. 
In Python, abstraction is achieved through abstract classes and interfaces, which serve as 
blueprints for other classes.

Key Idea
It allows the user to focus on what an object does rather than how it does it.
This is particularly helpful in reducing code complexity and improving modularity.

How to Implement Abstraction?
Python provides a module called abc (Abstract Base Classes) to implement abstraction. 
It allows you to create abstract methods that must be implemented in derived classes.

"""

print ("\n####################### Example-1 #################################################")
print ("""
Example: Abstraction with Animals
Let's say you want to create a program with animals that have different ways of making sounds. 
Using abstraction, you can define a blueprint for all animals without specifying the details.

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, no implementation here

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"  # Dog's implementation of make_sound

class Cat(Animal):
    def make_sound(self):
        return "Meow!"  # Cat's implementation of make_sound

# Polymorphism with abstraction
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())    

""")

from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class
    @abstractmethod
    def make_sound(self):
        pass  # Abstract method, no implementation here

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"  # Dog's implementation of make_sound

class Cat(Animal):
    def make_sound(self):
        return "Meow!"  # Cat's implementation of make_sound

# Polymorphism with abstraction
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())


print ("\n####################### Example-2 (Real-World Example: Payment System) ############")
print ("""
Imagine a payment system where different payment methods (e.g., Credit Card, PayPal) are implemented.
An abstract class can provide a common interface for these methods.
Explanation of the Code:
       "from abc import ABC, abstractmethod"
         The above line in code indicates: 
         1. The abc module (short for Abstract Base Classes) is imported.
         2. This module allows you to define abstract base classes in Python. An abstract base class 
             serves as a blueprint for other classes and cannot be instantiated directly.
         3. ABC is the base class for defining abstract classes, and abstractmethod is used to define 
            methods that must be implemented in subclasses.
       
        "class Payment(ABC):"
         The above line in code indicates:
         1. A class "Payment" is defined. It inherits from ABC, making it an abstract base class.
         2. This means Payment serves as template, and its purpose is to ensure that 
            all subclasses implement certain methods  
       
        "@abstractmethod
        "def process_payment(self,amount):"
            "pass"
         The above line in code indicates:
         1. Here, an abstract method process_payment is defined inside the Payment Class
         2. The @abstractmethod decorator ensures that any subclass of "Payment" must
            implement this method, otherwise, Python will raise an error.
         3. The "pass" keyword indicates that the method does not have an implementation here.
            It's just a placeholder to enforce implementation in subclasses 
       
What's Happening Overall
Abstract Class and Method:

The Payment class defines a blueprint for payment types. It ensures that subclasses like 
CreditCardPayment and PayPalPayment implement the process_payment method.

Polymorphism in Action:

The loop demonstrates polymorphism, where the same method (process_payment) behaves 
differently depending on the type of object (CreditCardPayment or PayPalPayment).

Code Modularity:

The abstraction makes the code modular and extensible. For example, you can easily 
add another payment method, like BankTransferPayment, without altering existing classes.
       """)
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

print ("####################################################################################\n")


