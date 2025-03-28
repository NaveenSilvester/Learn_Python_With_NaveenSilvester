"""
NUMERIC DATA TYPE IN PYTHON

Numeric Type:
	Integers (int): 
    •	Represents whole numbers, both positive and negative
    •	No fractional or decimal parts
    •	Example: 5, -12, 100, 50, 104

	Floating-Point Numbers (float):
    •	Represents real numbers that can have decimal points
    •	Can also be expressed using scientific notations (e.g. 1.2e3 for 1200)
    •	Example: 5.74, 90.12, -5.3, 1.34e4

	Complex Numbers (complex):
    •	Represents numbers with a real and imaginary part
    •	Written in the form a + bj, where a is the real part and b is the imaginary part
    •	Example: 3+4j, 1-2j
Each of these numeric types is a class in Python, and variables of these types are instances of their respective classes. You can use the type() function to check the data type of a value.

"""


#####################################################################################################################
## Integer Data Type
#####################################################################################################################
"""
What builtin functions can I use with Integers?
•	abs(): Returns the absolute value of the integer
print (abs(-10)) # Output = 10
•	pow(): Raises an integer to the power of another number. It also allows modulo operations as an optional third argument.
print (pow(2,3)) # Output: 8 
print (pow(2,3,5) # Output: 3    #2^3 % 5
•	divmod(): Returns a tuple containing the quotient and the remainder of the integer division.
print(divmod(10,3)) # Output: (3,1)
•	round(): Rounds an integer (or float) to a specified number of decimal places. Its useful when integers are mixed with other types during calculations.
print(round(5.98) # Output: 6
•	bin(): converts an Integer to its binary representation
print(bin(10)) # Output: 0b1010
•	hex(): Converts an integer to its hexadecimal representation
print(hex(255)) # Output: ‘0xff’
•	oct(): Converts an integer to its Octadecimal representation
print(oct(8)) # Output: ‘0010’
•	isinstance: Checks if the variable belongs to the int class
print(isinstance(42,int)) # Output: True

"""
a = 10
b = -100
c = 100

print (a)
print ("Data Type of a is ", type(a)) # Note: type() returns the data type of the variable
print ("Data Type of b is ", type(b))

print ("#######################################")
print ("Addition of Integers")
print ("#######################################")
addition = a + c
print ("Addition of 10 and 100 is: ", addition)
print ("Addition Data Type is: ", type(addition))

print ("\n#######################################")
print ("Multipiication of Integers")
print ("#######################################")
multiplication = a * c
print ("Multiplication of 10 *  100 is: ", multiplication)
print ("Multiplication Data Type: ", type(multiplication))

print ("\n#######################################")
print ("Division of Integers")
print ("#######################################")
print ("Division returns Float Value as the resultant Data Type")
division = c/a
print ("Division of 100 by 10 is: ", division)
print ("Division Data Type: ", type(division))
## Note: Division of integer results in Float

print ("\n#######################################")
print ("Floor Division of Integers")
print ("#######################################")
print ("Floor Division returns integer part of the division")
floordivision = c//a
print ("Floor Division of 100 // by 10 is: ", floordivision)
print ("FloorDivision Data Type is: ", type(floordivision))


print ("\n#######################################")
print ("Modulus Division of Integers")
print ("#######################################")
print ("Modulus returns Remainder of the division")
modulusdivision = 71%7
print ("Modulus Division of 71 // by 7 is: ", modulusdivision)
print ("Modulus Division Data Type is: ", type(modulusdivision))

print ("\n#######################################")
print ("divmod(): Returns a tuple of quotient and reminder")
print ("#######################################")
print("Div mod of 10, 3: ", divmod(10,3))

print ("\n#######################################")
print ("Built-In Functions that I can use with integers")
print ("#######################################")

print ("\n#######################################")
print ("abs()")
print ("#######################################")
print("Absolute value of -10.3: ", abs(-10.3))

print ("\n#######################################")
print ("pow()")
print ("#######################################")
print("Power of 2 to 3: ", pow(2,3))

print ("\n#######################################")
print ("bin()")
print ("#######################################")
print("Binary value of 28: ", bin(28))


print ("\n#######################################")
print ("isinstance()")
print ("#######################################")
print("isinstance of 28: ", isinstance(28, int))
