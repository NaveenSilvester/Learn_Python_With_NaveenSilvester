#####################################################################################################################
### Packages
#####################################################################################################################
"""
Packages
You can organize multiple modules into directories called packages. A package is a directory that contains an __init__.py. file. A package in Python is a collection of related modules grouped together in a directory. It helps organize code into a hierarchical structure, making it more manageable and modular for larger applications.

Key Features of a Package
1.	Directory-Based: A package is essentially a directory that contains one or more Python module files (.py).
2.	__init__.py File: Every package must include an __init__.py file (can be empty). It marks the directory as a Python package and can include initialization code.
3.	Nested Packages: A package can contain sub-packages, creating a hierarchical structure.

Structure of a Package
Imagine you're building an application for data processing. You can organize your code as follows:
data_processing/
    __init__.py        # Indicates this is a package
    reader.py          # Module for reading data
    writer.py            # Module for writing data
    processor.py  # Module for processing data

Creating and Using a Package
Step 1: Create a Directory
Create a directory for the package (e.g., data_processing).
Step 2: Add Modules
Inside the directory, add modules such as reader.py, writer.py, and processor.py.
Step 3: Add the __init__.py File
This file can be empty, or it can include code to initialize the package or expose specific components.
Example: __init__.py

Example: Creating a Package
1.	Directory Structure
data_processing/
    __init__.py
    reader.py
    writer.py
2.	Module: reader.py
def read_data(file_name):
    return f"Reading data from {file_name}"
	
3.	Module: writer.py
def write_data(file_name):
    return f"Writing data to {file_name}"
4.	Script to use the package
Save this file outside the package directory
import data_processing.reader as reader
import data_processing.writer as writer

print(reader.read_data("input.txt"))  # Output: Reading data from input.txt
print(writer.write_data("output.txt"))  # Output: Writing data to output.txt


"""


print("\n#################################################################################")
print ("################### Example-1 (Using a module named my_first_module) ########")
import my_first_module
#from my_first_module import *
print ("Using my_first_module and function named greet, with argument 'Allen' : \n", my_first_module.greet("Allen"))
print("#################################################################################\n")

