##################################################################################################
#### Class Attributes
##################################################################################################
"""
In Python, attributes of classes can have different levels of accessibility: public, protected, 
and private. These define how you can access and modify an attribute, and this is crucial for 
implementing encapsulation in object-oriented programming.

1. Public Attributes
Public attributes are accessible from anywhere—in the class, subclasses, or even outside the class. 
By default, all attributes in Python are public unless explicitly stated otherwise.
class PublicExample:
    def __init__(self):
        self.public_attribute = "I am Public"

example = PublicExample()
print(example.public_attribute)  # Accessible outside the class

In this example, public_attribute can be freely accessed and modified.


2. Protected Attributes
Protected attributes are meant to be accessed within the class and its subclasses. Python uses a 
single underscore _ prefix to denote protected attributes. However, it's not truly private—it's more 
of a convention to indicate that the attribute shouldn't be accessed directly.
class ProtectedExample:
    def __init__(self):
        self._protected_attribute = "I am Protected"

    def access_protected(self):
        return self._protected_attribute  # Accessible within the class

class Subclass(ProtectedExample):
    def modify_protected(self):
        self._protected_attribute = "Modified in Subclass"

example = ProtectedExample()
subclass = Subclass()
print(example._protected_attribute)  # Technically accessible, but discouraged

Here, _protected_attribute is suggested not to be accessed directly outside the class

3. Private Attributes
Private attributes are accessible only within the class where they are defined. Python uses a double 
underscore __ prefix to denote private attributes. This triggers name mangling, which means the attribute 
name is internally changed to include the class name as a prefix.
class PrivateExample:
    def __init__(self):
        self.__private_attribute = "I am Private"

    def access_private(self):
        return self.__private_attribute  # Accessible within the class

example = PrivateExample()
# print(example.__private_attribute)  # This will raise an AttributeError
print(example._PrivateExample__private_attribute)  # Access using name mangling
In this case, __private_attribute cannot be accessed directly outside the class. 
To access it, you need to use the name-mangled version (_ClassName__attributeName).


"""
print ("####################################################################################################################\n")

print ("\n####################### Example (Public Attribue):)###########################################################")
class PublicExample:
    def __init__(self):
        self.public_attribute = "I am Public"

example = PublicExample()
print(example.public_attribute)  # Accessible outside the class

print ("####################################################################################################################\n")



print ("\n####################### Example (Protected Attribue):)###########################################################")
class ProtectedExample:
    def __init__(self):
        self._protected_attribute = "I am Protected"

    def access_protected(self):
        return self._protected_attribute  # Accessible within the class

class Subclass(ProtectedExample):
    def modify_protected(self):
        self._protected_attribute = "Modified in Subclass"
        return self._protected_attribute

example = ProtectedExample()
subclass = Subclass()
print(example._protected_attribute)  # Technically accessible, but discouraged
print (subclass.modify_protected())
print(f"This is the best practice to access Protected Attributes : {example.access_protected()}")   # This is the best practice to access protected attributes
print ("####################################################################################################################\n")




print ("\n####################### Example (Private Attribue):)###########################################################")
class PrivateExample:
    def __init__(self):
        self.__private_attribute = "I am Private"
        self.__species = "Mammal"

    def access_private(self):
        return self.__private_attribute  # Accessible within the class

class Dog(PrivateExample):
    def __init__(self):
        super().__init__()
        self.__dog = "Canines"

    def get_dog(self):
        return (f"This is Dog and belong to {self._PrivateExample__species}  and {self.__dog}")    
        
example = PrivateExample()
# print(example.__private_attribute)  # This will raise an AttributeError
print(example._PrivateExample__private_attribute)  # Access using name mangling
print(example.access_private())

dog1 = Dog()
print(dog1.get_dog())
print ("####################################################################################################################\n")