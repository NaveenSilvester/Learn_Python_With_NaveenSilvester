#####################################################################################################################
### Functions - Recursive Functions in Python
#####################################################################################################################
"""
Recursive Functions
	These are functions that call themselves to solve smaller instances of a problem. Recursive functions in Python are functions that call themselves in order to solve problems. They break down complex problems into smaller sub-problems by repeatedly calling themselves until reaching a base case (the stopping condition)

Structure of a Recursive Function
1.	Base Case: The condition that stops the recursion
2.	Recursive Case: The function calls itself to solve a smaller problem

Example: Factorial Calculation
def factorial (n):
	# Base Case: Stop recursion when n is 0
	If n == 0
		return 1
	# Recursive Case: Multiply n by factorial of (n -1)
		return n * factorial(n-1)
print (factorial(5)) # Output: 120

Example: Fibonacci
def Fibonacci(n):
	# Base Cases
	if n == 0:
		return 0
	elif n == 1:
		return 1
	# Recursive Case
	return fibonacci(n -1) + Fibonacci(n-2)
print(Fibonacci(6)) # Output: 8 

Advantages of Recursion:
•	Simplifies code for problems involving repetitive tasks or divide-and-conquer strategies
•	Useful for tasks like traversing trees or solving mathematical problems
Disadvantages:
•	Can lead to excessive memory usage and slower performance for deep recursion.
•	Python imposes a recursion limit (usually 1000). You can check or modify it using.
Import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000) # Set a higher limit

"""

print("\n#################################################################################")
print ("################### Example-1 (Factorial) #######################################")
def factorial(n):
    if n == 0:
        #Base Case: Recursion to Stop
        return 1
    return n * factorial(n -1)
print ("Factorial of 5 is : ", factorial(5))
print("#################################################################################\n")



print("\n#################################################################################")
print ("################### Example-2 (Fibonacci) #######################################")
def fibonacci(n):
    if n == 0:
        #Base Case: Recursion to Stop
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n -2)
print ("Fibonacci of 5 is : ", fibonacci(999))
print("#################################################################################\n")

import sys
print(sys.getrecursionlimit())
