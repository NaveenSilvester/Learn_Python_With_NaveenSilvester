##################################################################################################
#### Composition Property in Object Oriented Programming
##################################################################################################
"""
Composition
Definition: Composition is the practice of designing a class that contains instances of other classes, rather than inheriting from them. It represents a "has-a" relationship.
Purpose: It provides flexibility and avoids the limitations of inheritance.

Example:
class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an engine

    def start(self):
        return self.engine.start()

my_car = Car()
print(my_car.start())  # Output: Engine started.


"""
print ("\n####################### Example-1 #################################################")
class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an engine

    def start(self):
        return self.engine.start()

my_car = Car()
print(my_car.start())  # Output: Engine started.
print ("####################################################################################\n")

print ("\n####################### Example-2 #################################################")
class Engine:
    def start(self):
        return "Engine started."

    def stop(self):
        return "Engine stopped."

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return self.engine.start()  # Delegating to Engine's method

    def stop_car(self):
        return self.engine.stop()  # Delegating to Engine's method

# Create an Engine object
engine = Engine()

# Pass the Engine object to Car
my_car = Car(engine)

print(my_car.start_car())  # Output: Engine started.
print(my_car.stop_car())   # Output: Engine stopped.
print ("####################################################################################\n")


print ("\n####################### Example-3 #################################################")
class Animal:
    def species(self):
        return ("Animal species is Mammal")

class Dog:
    def __init__(self):
        self.Animal = Animal() # Composition of class
    
    def myspecies(self):
        return self.Animal.species()
        

dog = Dog()
print(dog.myspecies())
print ("####################################################################################\n")
