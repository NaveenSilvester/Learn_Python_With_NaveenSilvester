#####################################################################################################################
### Functions - Lambda Functions in Python
#####################################################################################################################

"""
Lambda (Anonymous) Functions
	These are small, anonymous functions created using the lambda keyword. They are typically used for short, single-expression operations.
Syntax: lambda arguments: expression
Lambda functions can take any number of arguments but only have a single expression.
Example-1
square = lambda x : x ** 2
print(square(5) # Output: 25
Explanation: The lambda function takes one argument “x” and returns x ** 2
Example-2
Using lambda function with python’s filter() to get even number from a list
numbers = [1,2,3,4,5,6,7,8]
even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers) # Output: [2,4,6,8]

Example-3
Use a lambda function with Python’s map() to convert temperature from Celcius to Fahrenheit
celsius = [0,10,20,30]
fahrenheit = list(map(lambda x : (x * 9/5) + 32, celsius))
print(fahrenheit) # Output: [32.0, 50.0, 68.0, 86.0]

Example-4
Use a lambda function with Python’s reduce() to compute the product of numbers in a list.
from functools import reduce
numbers = [1,2,3,4,5]
product = reduce(lambda x, y: x * y, numbers)
print(product) # Output: 120

"""
print("\n#################################################################################")
print ("################### Example-1 ###################################################")
squares = lambda x : x ** 2
print(f"Square of 5 is {squares(5)}")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-2 ###################################################")
print ("Get Even numberes a list")
my_list = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x : x % 2 == 0, my_list))
print("Even Numbers in the list are: ", even_numbers)
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-3 ###################################################")
print ("Convert a list of Temperatures from Celsius to Fahrenheit")
celsius = [0,10,20,30]
fahrenheit = list(map(lambda x : (x * 9/5 ) + 32, celsius))
print("The celsius [0,10,20,30] converted do Fahreneheit is : ", fahrenheit)
print("#################################################################################\n")



print("\n#################################################################################")
print ("################### Example-4 ###################################################")
print ("Cummulative Product of a list of numbers")
from functools import reduce
numbers = [1,2,3,4,5]
product = reduce(lambda x,y : x * y, numbers)
print (f"The cummulative product of 1,2,3,4,5 is : {product}")
print("##################################################################################\n")

