##################################################################################################
#### Design Pattern - Creational Design - Singleton
##################################################################################################
print ("\n####################################################################################################################")
print (""" Description:
                                        Design Pattern - Creational Design
Creational design patterns focus on object creation mechanisms, aiming to make the process flexible and reusable while hiding 
       complex instantiation logic.
       """)
print ("####################################################################################################################\n")


print ("\n#####################################################################################################################")
print ("####################### Creational Design - Singleton ################################################################")
print ("""
Notes:
       Singleton: Ensures only one instance of a class exists and provides a global access point to it.
""")
print ("#####################################################################################################################")


print ("\n#####################################################################################################################")
print ("####################### Example-1 (Singleton Creational Design) #######################################################")
print (""" Explantion of the code:
	Class Variable _instance
       _instance = None
The _instance class variable is used to store the single instance of the Singleton class. Initially, it is set to None.

 __new__ method
              def __new__(cls):
              if cls._instance is None:
                     cls._instance = super(Singleton, cls).__new__(cls)
              return cls._instance

What is __new__?
Its a special method in Python that is responsible for creating a new instance of the class before the __init__ method is called.

What happens here?
When Singleton() is called, it checks whether _instance is None.
If the _instance is None (no instance exists yet), it creates a new instance using super(Singleton, cls).__new__(cls) and assigns it to _instance.
If the _instance already exists, it skips creation and returns the existing instance.

Creating Singleton Object
singleton1 = Singleton()
singleton2 = Singleton()
  Here, two objects (singleton1 and singleton2) are created from the Singleton class.
  Both objects will refer to the same instance because the __new__ method ensures that _instance is reused instead of creating a new one.

Comparing Instances
print(singleton1 is singleton2)  # Output: True
""")
print ("#####################################################################################################################")
print ("Code Output:")
class Singleton():
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print (singleton1 is singleton2)
print ("\n#####################################################################################################################")

