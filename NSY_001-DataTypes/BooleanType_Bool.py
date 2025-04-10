#####################################################################################################################
## Boolean Data Type
#####################################################################################################################
"""
	In Python, the Boolean data type represents one of two values: Ture or False. These values are used to evaluate conditions and make decisions in your code.
Key Features of Booleans in Pythons
1.	Data Type: Booleans are a fundamental data type in Python and are subclassed from integers. Internally:
True is equivalent to 1
False is equivalent to 0
2.	Logical Operations: Booleans are used in logical operations like and, or, and not.
Example:
a = True
b = False
print (a and b) # Output: False
print (a or b) # Output: True
print (not a) # Output: False
3.	Comparisons Result in Booleans: When you compare values in Python, the result is a Boolean (True or False). Example
x = 10
y = 20
print (x < y) # Output: True
print(x == y) # Output: False
4.	Truthy and Falsy Values: Many data types can be evaluated as True, or False:
Falsy values: 0, None, empty objects ([],{},””)
Truthy values: Any non-zero number or non-empty object. Example:
print(bool(0)) # Output: False
print(bool(42)) # Output: True
print(bool([]) #Output: False
print(bool([1,2,3])) # Output: True
Why Booleans Matter:
	Booleans play a critical role in conditional statements (if, while, etc.,), allowing programs to make decisions and execute code based on conditions.

"""
###############################################################################
### Boolean Data Type Examples
###############################################################################
print("\n####################################################################")
print ("################### Example-1 Boolean Data Type ####################")
print ("Boolean a = True, b = False")
a = True
b = False
print ("Boolean a evaluates to : ", a)
print ("Boolean b evaluates to : ", b)
print("##################################################################\n")

print("\n########################################################################################")
print ("################### Example-2 Logical Operation on Boolean Data Type ###################")
print (" Boolean of (a and b ) evaluates to : ", ( a and b))
print (" Boolean of (a or b ) evaluates to : ", ( a or b))
print (" Boolean of (not a ) evaluates to : ", ( not a))
print("#######################################################################################\n")

print("\n########################################################################################")
print("################### Example-3 Comparison on Boolean Data Type ##########################")
a = 2
b = 4
print (" Boolean of a = 2  b = 4, a < b evaluates to : ", ( a < b))
print (" Boolean of a = 2  b = 4, a > b evaluates to : ", ( a > b))
print (" Boolean of a = 2  b = 4, a ==  b evaluates to : ", ( a == b))
print("########################################################################################\n")


print("\n########################################################################################")
print("################### Example-4 Truthy and Falsy Values ###################################")
print('''Many data types can be evaluated as True, or False:
         Falsy values: 0, None, empty objects ([],{},"")
         Truthy values: Any non-zero number or non-empty object.
''')
print("Value of bool(0) : ", bool(0)) # Output: False
print("Value of bool(42) : ", bool(42)) # Output: True
print("Value of bool[] : ", bool([])) #Output: False
print("Value of bool([1,2,3]) : ", bool([1,2,3])) # Output: True
print("########################################################################################\n")

print("\n########################################################################################")
print("################### Example-5 Combining Operators #######################################")
age = 35
has_license = True

can_drive = age > 18 and has_license
print ("Age of the individual is age = 35 and has_license = True, (age > 18 and has_license) evaluates to : ", can_drive)
print("########################################################################################\n")


print("\n##############################################################################################################")
print("################### Example-6 Combining Operators Short Circuit Behavior #######################################")
print ('''
        and: Stops evaluating as soon as it encounters a False value because the result is already False.
        or: Stops evaluating as soon as it encounters a True value because the result is already True.
''')
x = 5
print ("Note: x = 2, (x > 2  and x < 5), evaluates : ", (x > 2 and x < 5))
print ("Note: x = 2, (x > 2  or x < 5), evaluates : ", (x > 2 or x < 5))
print("##############################################################################################################\n")
