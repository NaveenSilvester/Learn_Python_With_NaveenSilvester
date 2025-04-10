##################################################################################################
#### Object Oriented Programming in Python
##################################################################################################

"""
Object Oriented Programming (OOP) is a programming paradigm based on the concept of “objects”, 
which can contain data and methods to operate on that data. In Python, OOP provides a structured 
approach to design programs by organizing related data and functions together.
Key Concepts of OOP in Python
1.	Classes and Objects
A Class is a blueprint for creating objects. It defines the structure and behavior that the object will have.
An Object is an instance of class, representing a specific entity.
Example:
class Dog:
	def __init__(self, name, breed):
		self.name = name
		self.breed = breed
	def bark(self):
		return (f”{self.name} says Woof!”)

# Creating objects
dog1 = Dog(“Buddy”, “Golden Retriever”)
print(dog1.bark) # Output: Buddy says Woof!

2.	Encapsulation
Encapsulation is building data (attributes) and methods (functions) within a class. It hides the implementation details and allows controlled access using methods. Encapsulation involves bundling data (attributes) and methods that operate on the data within one unit (class). It helps protect object attributes using access modifiers like private (_attributes) and public (attributes) attributes.
class BankAccount:
	def __init__(self, balance):
		self.balance = balance # Protected Attribute
	def get_balance(self):
		return self._balance
	account = BankAccount(1000)
	print(account.get_balance()) # Output: 1000 
3.	Inheritance
Inheritance allows a class (child class) to derive properties and methods from another class (parent class)
It facilitates code reuse and provides hierarchical structure
Example:
class Animal:
	def __init__(self, species):
		self.species = species
	def describe(self):
		print(f”I am a {self.species}.”)

class Cat(Animal): # Inherits from Animal Class
	def __init__(self,name):
		super().__init__(“Cat”)
		self.name = name
	def speak(self):
		print(f”{self.name} says Meow!”)
	
	fluffy = Cat(“Fluffy”)
	fluffy.describe() # Output : I am a Cat
	fluffy.speac() # Output: Fluffy say Meow! 


4.	Polymorphism
Polymorphism allows methods in different classes to be used interchangeably through method overriding or interface implementation.
Example:
class Bird:
	def __init__(self):
		print(“Tweet!”)
class Dog:
	def speak(self):
		print(“Woof!”)

def animal_sound(animal):
	animal.speak()

animal_sound(Bird()) # Output: Tweet!
animal_sound(Dog()) # Output: Woof!

5.	Abstraction
Abstraction simplifies complex systems by hiding implementation details while exposing functionalities.
Example:
from abc import ABC, abstractmethod
class Vechicle(ABC):
	@abstractmethod
	def drive(self):
		pass
class Car(Vehicle):
	def drive(self):
		print(“Driving a Car!”)
car = car()
car.drive() # Output: Driving a Car! 

"""

print ("\n####################### OBJECT ORIENTED PROGRAMMING ################################")
print ("###################### CLASS AND OBJECT ###########################################\n")
print ("""A Class is a blueprint for creating objects. It defines the structure and behavior 
       that the object will have.
        An Object is an instance of class, representing a specific entity.
       """)
print ("####################################################################################\n")

print ("\n####################### OBJECT ORIENTED PROGRAMMING ################################")
print ("###################### Example -1 CLASS AND OBJECT ##################################\n")
class Dog:
    def __init__(self, breed):
        self.breed = breed


    def bark(self):
        print("Dog Barks Bow Bow!")


    def breedname(self):
        print(f"My Dog breed is {self.breed}")

mydog = Dog("Pug")
mydog.bark()
mydog.breedname()
print ("####################################################################################\n")

print ("\n####################### OBJECT ORIENTED PROGRAMMING ################################")
print ("###################### Example -2 Encapsulation ##################################\n")
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def get_balance(self):
        return self.balance

myaccount = BankAccount(1000)
print(f"My Bank Account Balance is : {myaccount.get_balance()}")
print ("####################################################################################\n")



print ("\n####################### OBJECT ORIENTED PROGRAMMING ################################")
print ("###################### Example -3 Inheritance #######################################\n")

class Animal():
    def __init__ (self,species):
        self.species = species
    
    
    def describe(self):
        print(f"I am {self.species}\n")



class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")
        self.name = name
    
    def speak(self):
        print(f"{self.name} says Meow!")

mycat = Cat("Fluffy")
mycat.describe()
mycat.speak()

print ("####################################################################################\n")

print ("\n####################### OBJECT ORIENTED PROGRAMMING ################################")
print ("###################### Example -3 Polymorphism #######################################\n")

class Bird:
    def speak(self):
        print("Tweet!")

class Dog:
    def speak(self):
        print("Woof!")

def animal_sound(var):
    var.speak()

animal_sound(Bird())
animal_sound(Dog())
print ("####################################################################################\n")

print ("\n####################### OBJECT ORIENTED PROGRAMMING ################################")
print ("###################### Example -4 Polymorphism #######################################\n")

class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"I'm {self.name} - I make Tweet Sound!")

class Dog:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"I am {self.name}, I make Woof sound")

def animal_sound(var):
    var.speak()

animal_sound(Bird("Parrot"))
animal_sound(Dog("Dog"))
print ("####################################################################################\n")

print ("\n####################### OBJECT ORIENTED PROGRAMMING ################################")
print ("###################### Example -5 ##################################################\n")
class vehicle:
    def __init__(self,brand, year):
        self.brand = brand
        self.year = year
    
    def get_brand(self):
        return(f"Name of the Car Brand is {self.brand}")
    
    def get_year(self):
        return(f"Year of Manufacture : {self.year}")

    def get_details(self):
        return (f"Name of the car brand is {self.brand} manufactured in the year {self.year}")


my_vehicle = vehicle("Creta", "2019")
print (my_vehicle.get_brand())
print (my_vehicle.get_year())
print (my_vehicle.get_details())
print ("####################################################################################\n")





