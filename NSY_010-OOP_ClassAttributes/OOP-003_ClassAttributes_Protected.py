##################################################################################################
#### Class Attributes - Protected Attribute
##################################################################################################
print ("\n####################################################################################################################")
print ("""
                                Protected Attributes
Protected attributes are meant to be accessed within the class and its subclasses. Python uses a single underscore _  prefix to denote protected attributes. However, its not truly private – it’s more of a convention to indicated that the attribute should not be accessed directly.

What are Protected Attributes?
Protected attributes are declared with a single underscore (_) prefix before the attribute name. For example: _attribute_name. This convention signals that the attribute should not be accessed directly outside the class or its subclasses. However, technically, they can still be accessed outside if needed.

Characteristics of Protected Attributes
Access Visibility:
•	Accessible within the class where they are declared.
•	Accessible in subclasses of the class.
•	Technically accessible outside the class, but it’s discouraged as per convention.
Soft Restriction:
•	The single underscore is a convention, not enforced by Python. It's more of a "gentle reminder" to developers.

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
print(subclass._modify_protected()) # Modified subclass or child class
	
Why Use Protected Attributes?
1.	Encapsulation: Ensures the internal representation of an object is hidden from the outside.
2.	Code Clarity: Signals to other developers that certain attributes shouldn’t be accessed directly.
3.	Prevents Unintended Changes: Reduces the risk of accidental modification of critical attributes from outside the class
Summary
Protected attributes (_attributes) are a Python convention to limit direct access from outside a class. They strike a 
       balance between flexibility and encapsulation, making them an essential tool in object-oriented programming.
       """)
print ("####################################################################################################################\n")


print ("\n#####################################################################################################################")
print ("####################### Example (Protected Attribute) ################################################################")
print ("#####################################################################################################################")

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
print(subclass.modify_protected()) # Modified subclass or child class
print(f"The right way to access protected attribute from parent class is : {example.access_protected()}")
print ("####################################################################################################################\n")
