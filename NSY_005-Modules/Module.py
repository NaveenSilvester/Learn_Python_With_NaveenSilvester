#####################################################################################################################
### Modules
#####################################################################################################################
"""
Modules
Modules in Python are files that contain Python Code, such as functions, classes, and variables, which can be reused across multiple programs. They help organize code into manageable and reusable components.
Key Features of Python Modules:
1.	Code Reusability: Modules allow you to reuse code instead of rewriting it.
2.	Simplified Maintenance: By splitting code into smaller files, it becomes easier to manage and debug.
3.	Built-in and Custom Modules: Python provides built-in modules (e.g., math, os) and allows you to create your own.
Types of Modules:
1.	Standard Modules: Pre-installed modules like math, random, os
2.	Third-Party Modules: Modules that can be installed using package managers like pip (e.g., numpy, pandas)
3.	Custom Modules: Created by users for specific community
Using Modules
You can use the import statement to include modules in your program
Example:
	# Importing the math module
	import math
	print(math.sqrt(16)) # Output: 4.0
Creating Custom Modules
You can create your own module by writing Python Code in a file (e.g., my_module.py)
Example: my_module.py
	def greet(name):
return (f”Hello {name}, Welcome to Learning Python Programming with NaveenSilvester
!”)
Using Custom Modules
	import my_module
	print(greet(“Allen”) # Output: Hello Allen, Welcome to Learning Python Programming with NaveenSilvester!

Best Practices
1.	Keep modules small and focused on a single purpose.
2.	Use descriptive names for modules to reflect their functionality
3.	Avoid using * imports to prevent name conflicts
4.	Organize related modules in to packages for better maintainability

"""


print("\n#################################################################################")
print ("################### Example-1 (Using a module named my_first_module) ########")
import my_first_module
#from my_first_module import *
print ("Using my_first_module and function named greet, with argument 'Allen' : \n", my_first_module.greet("Allen"))
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-2 (Using a module named my_math_module) ########")
import my_math_module
#from my_first_module import *
print ("Here is the sum and product of 2, 3 : ", my_math_module.AddandMultiply(2,3))
print ("Here is the Square of 5 : ", my_math_module.square(5))
print ("Here is the Cube of 5 : ", my_math_module.cube(5))
print ("Here is the factorial of 5 : ", my_math_module.factorial(5))
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-3 (Using a module alias) ############################")
import my_math_module as m
#from my_first_module import *
print ("Here is the sum and product of 2, 3 : ", m.AddandMultiply(2,3))
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-4 (Imporing specific function in module) ##############")
from my_math_module import square 
print ("Here is the Square of 17 : ", my_math_module.square(17))
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-5 (Accessing Module attributes) #####################")
import my_math_module
print ("Here are the Attributes of the Module ", dir(my_math_module))
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-6 (Help on Module attributes) #####################")
import my_math_module
print ("Here are the Help documentation of the Module ", help(my_math_module))
print("#################################################################################\n")
