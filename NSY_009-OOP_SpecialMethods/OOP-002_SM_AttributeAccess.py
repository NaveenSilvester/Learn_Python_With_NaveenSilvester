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