#####################################################################################################################
## Float Data Type
#####################################################################################################################
"""
Floating-Point Numbers (float):
•	Represents real numbers that can have decimal points
•	Can also be expressed using scientific notations (e.g. 1.2e3 for 1200)
•	Example: 5.74, 90.12, -5.3, 1.34e4

Performance Considerations while using Float
Using the float data type in Python is convenient for handling real numbers, but there are a few performance and accuracy considerations to keep in mind.
1.	Precision Loss: Floats are represented in binary format internally, which can cause rounding errors, especially with very large or very small numbers. For instance:
0.1	+ 0.2 # Output: 0.30000000004
These inaccuracies can propagate in complex calculations
2.	Memory Usage: Floats consume more memory than integers. In Python, a flot typically uses 64 bits, which might not be ideal if memory is a constraint and you can work with integers instead.
3.	Performance: Arithmetic operations on floats can be slower than on integers, as floating-point arithmetic requires computational resources. If your application involves intensive numerical computations, this could impact performance.
4.	Comparisons: Comparing floating-point numbers for equality can be unreliable due to precision issues. It’s better to check if the numbers are “close enough” using a small tolerance:
import math
math.isclose(0.1 + 0.2, 0.3) # Output: True
5.	Alternatives:
For high precision: Use the decimal module, which avoids some floating-point inaccuracies by representing numbers exactly.
For large-scale numerical computations: Use specialized libraries like NumPy, which optimize floating-point performance for arrays and matrices.

"""


print ("#######################################")
print ("Addition of Floats")
print ("#######################################")
a = 3.14
b = -0.76
c = 2.0
addition = a + b
print ("Addition of 3.14 and 2.0  is : ", a + c)
print ("Data Type of variable Addition is: ", type(addition))


print ("\n#######################################")
print ("Multiplication of Floats")
print ("#######################################")
multiplication = a + b * c
print ("Multiplication of 3.14 and -0.76  is : ", a * b)
print ("Data Type of variable Multiplication is: ", type(multiplication))
#print("Result: ", result)

print ("\n#######################################")
print ("Division of Floats")
print ("#######################################")
division = 5.0 / 3.0
print ("Division of 5.0 by 3.0 is: ", division)
print ("Data Type of variable Division is: ", type(division))


print ("\n#######################################")
print ("Avoid Comparisons of Floats")
print ("Avoid Equality Comparison, becasue of precision issues, comparing floats directly can lean to unexpected results")
print ("#######################################")

a = 0.1 + 0.2
b = 0.3
print ("Comparison of two variables a = 0.1 + 0.2 and b = 0.3, the results says they are not equal")
print(a == b)


C1 = 5 + 3j
C2 = -2 + 4j
Addition = C1 + C2
Subtraction = C1 - C2
Multiplication = C1 * C2

print("Value of Addition variable is: ", Addition) # Output: 
print("Value of Subtraction variable is: ", Subtraction) 
print("Value of Multiplication variable is: ", Multiplication)  
