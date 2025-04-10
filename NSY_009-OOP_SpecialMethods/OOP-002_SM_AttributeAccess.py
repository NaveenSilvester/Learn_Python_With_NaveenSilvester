##################################################################################################
#### Special Methods - Attribute Access
##################################################################################################
"""
1.	_getattr__(self, name): Called when accessing an attribute that doesn’t exist.
2.	__setattr__(self, name, value): Called when setting an attribute.
3.	__delattr__(self, name): Called when deleting an attribute.

"""

print ("\n####################### Notes(__getattr__(self):)###########################################################")
print ("""
1.	_getattr__(self, name): Called when accessing an attribute that doesn’t exist.
The __getattr__() method in Python is a special method used to define behavior when an attribute that does not exist in an object is accessed. It acts as a fallback mechanism for undefined attributes and is invoked automatically.

Key Features of __getattr__()
1.	Triggered Only for Missing Attributes:
It is called when attempting to access an attribute that is not defined in the object. For attributes that are already defined, __getattr__() is not invoked.
2.	Dynamic Behavior:
It allows you to create dynamic or computed attributes on the fly.
3.	Common Use Cases:
1.	Implementing proxies or fallback attributes.
2.	Dynamically generating values or delegating functionality.

""")
print ("####################################################################################################################\n")

print ("\n####################### Example-1 (__getattr__(self):)###########################################################")
print ("""
Note:
       In this example, super().__getattribute__(attr) calls the original behavior of __getattribute__, 
       allowing normal attribute access. If an attribute isn't found, the code returns "attr is not defined".
       """)
print ("####################################################################################################################\n")
class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __str__(self):
        return f"School Name is {self.name} \nLocation is: {self.location}"
    
    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            return f"{attr} is not defined"

my_school = School("SJBHS", "Bangalore")
print(my_school)
print(my_school.name)
print(my_school.principal)
print ("####################################################################################################################\n")


print ("\n####################### Notes(__setattr__(self,name,value):)###########################################################")
print ("""
1.	__setattr__(self, name, value): Called when setting an attribute.
The __setattr__ method in Python is a special method used to define how attribute assignment (self.attribute_name = value) is handled in a class. When you override this method, you can customize how attributes are set in your class. This method intercepts all attempts to set attributes and provides you control over the assignment behavior.

Syntax:
def __setattr__(self, name, value):
    # Custom logic here
    super().__setattr__(name, value)  # Ensures attributes are properly set

Example:
class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)  # Use the default behavior to set the attribute

# Example usage:
my_school = School("Greenwood High", "Bengaluru")
print(my_school.name)  # Output: Greenwood High

Explanation:
•	When you create an instance of the School class and set the attributes name and location, the overridden __setattr__ method is called.
•	It prints a message each time an attribute is set.
•	super().__setattr__(name, value) is used to ensure that attributes are actually set on the object. Without this line, attributes would not be saved to the instance.
Use Cases:
1.	Logging or Tracking: Monitor all attribute changes in your object.
2.	Validation: Check the value of the attribute before assigning it (e.g., only accept positive numbers or strings of a specific format).

""")
print ("####################################################################################################################\n")
print ("\n####################### Example-1 (__setattr__(self, name, value):)##################################################")
class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)  # Use the default behavior to set the attribute

# Example usage:
my_school = School("Greenwood High", "Bengaluru")
print(my_school.name)  # Output: Greenwood High
print ("####################################################################################################################\n")


print ("####################################################################################################################\n")
print ("\n####################### Example-2(__setattr__(self, name, value):)##################################################")
class Family:
    def __init__(self, father, mother, son):
        self.father = father
        self.mother = mother
        self.son = son
    
    def __str__(self):
        return(f"Father name {self.father}, Mother name {self.mother} and Son name {self.son}\n")

    def __repr__(self):
        return(f"Family(father = '{self.father}', mother = '{self.mother}', son = '{self.son}')")

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            return f"{attr} is not defined"        
        

# Example usage:
my_family = Family("Raja", "Rani", "Yuvaraja")
print (my_family)  
print (f"Repr help is : \n {my_family.__repr__()}")
print(my_family.daughter)
print ("####################################################################################################################\n")


print ("\n####################### Notes(__delattr__(self,name):)###########################################################")
print ("""
The __delattr__ method in Python is a special method used to define how attributes are deleted from a class instance using the 
       del keyword. When you override this method, you can customize the behavior that happens when an attribute is deleted.
Syntax:
    def __delattr__(self, name):
        # Custom logic here
        super().__delattr__(name)  # Ensures attribute deletion
""")

print ("####################################################################################################################\n")
print ("\n####################### Example-1 (__delattr__(self, name):)##################################################")
print ("""
Note:
    Explanation:
When you use the del keyword, e.g., del my_school.name, the overridden __delattr__ method is invoked.
It prints a custom message before deleting the attribute.
The super().__delattr__(name) ensures that the attribute is actually removed from the object. 
Without this line, the attribute would not be deleted.
""")
class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __delattr__(self, name):
        print(f"Deleting the attribute: {name}")
        super().__delattr__(name)  # Perform the actual deletion

# Example usage:
my_school = School("Greenwood High", "Bengaluru")
del my_school.name  # This will call the overridden __delattr__
print(my_school.location)
print(my_school.name)