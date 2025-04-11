##################################################################################################
#### Class Attributes - Public Attribute
##################################################################################################
print ("\n####################################################################################################################")
print ("""
                                Public Attributes
Public attributes are accessible from anywhere in the class, subclasses, or even outside the class. 
       By default, all attributes in Python are public unless explicitly stated otherwise.
Example:
	class PublicExample:
		def __init__(self):
			self.public_attribute = “I am Public”
	
example = PublicExample()
print(example.public_attribute) # Accessible outside the class
       """)
print ("####################################################################################################################\n")


print ("\n####################################################################################################################")
print ("####################### Example (Public Attribute) ##################################################################")
print ("####################################################################################################################\n")
class PublicExample:
    def __init__(self):
        self.public_attribute = "I am Public"

example = PublicExample()
print(example.public_attribute)  # Accessible outside the class
print ("\n####################################################################################################################")


print ("\n####################################################################################################################")
print ("####################### Example (Public Attribute) ##################################################################")
print ("##################### Accessing Public Attribute of Parent Class #####################################################")
print ("####################################################################################################################\n")
class Parent:
    def __init__(self):
        self.public_attribute = "I am a public attribute of Parent"

class Child(Parent):
    def __init__(self):
        super().__init__()  # Initialize Parent class attributes
        self.child_attribute = "I am an attribute of Child"

    def access_parent_public(self):
        return self.public_attribute  # Access Parent's public attribute

# Create an instance of Child
child_instance = Child()

# Accessing Parent's public attribute directly via Child
print(f"Accessing Parent's public attribute directly via Child {child_instance.access_parent_public()}")  # Output: "I am a public attribute of Parent"

# Accessing Parent's public attribute directly
print(f"Accessing Parent's public attribute directly {child_instance.public_attribute}")  # Output: "I am a public attribute of Parent"

print ("\n####################################################################################################################")