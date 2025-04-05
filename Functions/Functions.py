#####################################################################################################################
### Functions in Python
#####################################################################################################################

"""
Functions in Python are blocks of reusable code that performs specific tasks. They help make your code modular, organized, and easier to maintain by allowing you to avoid repetition. Python supports user-defined functions, as well as built-in functions like print(), len() and others

Syntax of a Function:
To define a function in Python, you use the def keyword followed by the function name, parentheses (which may contain parameters), and a colon. The function’s block is indented.
def function_name(parameters):
	# Block of code
	return value
	Key Components:
1.	Function Definition: Use of def keyword to create a function
2.	Function Name: Used to identify the function
3.	Parameters: These are inputs the function can take (Optional)
4.	Code Block: The logic enclosed within the function
5.	Return Statement: The return keyword specifies the output of the function
Defining and Calling a function:
	def greet(name):
		return (f“Welcome {name}”)
	message = greet(“Allen”)
	print(message) # Output: Welcome Allen

Types of Functions:
1.	Built-in functions: These are predefined by Python and include functions like len(), sum(), max(), etc.,
Example: print(“Hello World”) 
2.	User-defined functions: Functions written by developers for specific tasks
Example: 
	def square(x):
		return x * x
	print(square(4)) # Output : 16
3.	Lambda Functions: Anonymous functions created with the lambda keyword for short-term use.
square = lambda x: x * x
print(square(4)) # Output: 16
4.	Recursive Functions: Functions that call themselves to solve smaller instances of the same problem
def factorial(n):
	if n == 1:
		return 1
	return n * factorial (n-1)
print(factorial(5)) # Output: 120
Benefits of using functions:
1.	Code Reusability: Write once, use multiple times.
2.	Modularity: Divide your program into smaller, manageable pieces
3.	Readability: Functions make your code easier to read and understand
4.	Easy Debugging: Errors can be isolated to specific functions.

Best Practices for Writing Functions
1.	Keep Functions Small: Each function should perform one specific task.
2.	Use Meaningful Names: Function names should clearly indicate what the function does.
3.	Minimize Side Effects: Avoid modifying global variables within functions.
4.	Document Your functions: Use docstrings to explain the purpose, inputs, and outputs of the function
5.	Handle Exceptions: Include error-handling mechanisms when dealing with external inputs.

Writing Functions with Documentation
		Python uses docstrings to document function. A docstring is a multiline string enclosed within triple quates (“””) placed directly below the function definition.
Example-1:
def calculate_area(length, width):
    
    # Calculate the area of a rectangle.
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    Returns:
    float: The calculated area of the rectangle.
    
    return length * width
# Using the function
print(calculate_area(10, 5))  # Output: 50
Example-2:
	from statistics import mean, median, mode
def calculate_statistics(numbers):
    
    # Calculate mean, median, and mode for a list of numbers.
    # Parameters:
    # numbers (list): A list of integers or floats.
    # Returns:
    # dict: A dictionary with keys 'mean', 'median', and 'mode' containing their respective values.
    # Raises:
    # ValueError: If the input list is empty.
    
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")

    return {
        "mean": mean(numbers),
        "median": median(numbers),
        "mode": mode(numbers)
    }

# Example usage
data = [1, 2, 3, 4, 4]
stats = calculate_statistics(data)
print(stats)
# Output: {'mean': 2.8, 'median': 3, 'mode': 4}
This function has:
•	A clear docstring to describe its purpose, parameters, return value, and exceptions.
•	Error handling using raise to ensure input validation.

Writing Functions with Test Cases
Test cases help ensure that your function behaves as expected. Python's unittest module is commonly used for this purpose.
Example:
import unittest
# Function to test
def add(a, b):
    # Add two numbers and return the result.
    return a + b
# Test cases
class TestAddFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(3, 7), 10)

    def test_negative_numbers(self):
        self.assertEqual(add(-3, -7), -10)

    def test_mixed_numbers(self):
        self.assertEqual(add(-3, 7), 4)
if __name__ == "__main__":
    unittest.main()

	Example-2:
import unittest

class TestCalculateStatistics(unittest.TestCase):
    def test_valid_data(self):
        data = [1, 2, 3, 4, 4]
        expected = {"mean": 2.8, "median": 3, "mode": 4}
        self.assertEqual(calculate_statistics(data), expected)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_statistics([])

    def test_single_value(self):
        data = [10]
        expected = {"mean": 10, "median": 10, "mode": 10}
        self.assertEqual(calculate_statistics(data), expected)

    def test_identical_values(self):
        data = [5, 5, 5]
        expected = {"mean": 5, "median": 5, "mode": 5}
        self.assertEqual(calculate_statistics(data), expected)

if __name__ == "__main__":
    unittest.main()

Key Features of the Test Cases
1.	Positive Cases: Ensure that the function works with typical inputs.
2.	Edge Cases: Test with unusual inputs, like an empty list or single-item lists.
3.	Error Handling: Verify that appropriate exceptions are raised for invalid inputs.

Key Benefits of Documentation and Test Cases
•	Documentation: Helps other developers (and your future self) understand the function's purpose, usage, and behavior.
•	Test Cases: Ensures reliability and correctness of the function across different scenarios.

"""


###############################################################################
### Functions
###############################################################################
print("\n#################################################################################")
print ("################### Example-1 Simple Function ###################################")
def hello():
    return ("Hello World!")
print("Calling the Function hello() : ", hello())
    
print("##################################################################################\n")


print("\n#################################################################################################")
print ("################### Example-2 Simple Function with parameters ###################################")
def greet(x):
    return (f"Hello {x} welome to the World Of Python Programming!")
print("Calling the Function greet('Allen') : ", greet("Allen"))    
print("###################################################################################################\n")

print("\n##########################################################################################################")
print ("################### Example-3 Simple Function with Multiple parameters ###################################")
def maths(a,b):
        sum = a + b
        prod = a * b
        return (f"{(sum, prod)}")
print("Output from function maths(a,b)  where a = 2, b = 3 is (sum, product): ", maths(2,3))    
print("############################################################################################################\n")

print("\n##########################################################################################################")
print ("################### Example-4 Simple Function with Default parameters ####################################")
print("The default parameters need to be mentioned after the regular parameters")
def circle(r, pi=3.14 ):
        area = pi * r * r
        circum = 2 * pi * r
        return (f"{(area, circum)}")
print("Output from function circle(a,b)  where r = 3 is (area, circum): ", circle( r = 3))    
print("############################################################################################################\n")

print("\n##########################################################################################################")
print ("################### Example-5 Simple Function returning multiple values ####################################")
print("The default parameters need to be mentioned after the regular parameters")
def rectangle(l, b ):
        area = l * b
        perimeter = 2 * (l + b)
        return (f"{(area, perimeter)}")
print("Output from function rectangle(a,b)  where l = 3 b = 2 is  (area, perimeter): ", rectangle( 3,2))    
print("############################################################################################################\n")


print("\n##########################################################################################################")
print ("################### Example-5 Recursive Function #########################################################")
print("Functions that call themselves to solve smaller instances of the same problem.")
def factorial(n):
      if n == 1:
        return 1
      return n * factorial (n-1)
print("Factorial of 4 is factorial(4) : ", factorial(4))
          
print("############################################################################################################\n")


print("\n##########################################################################################################")
print ("################### Example-6 Writing Function with Documentation ########################################")
print("""Python uses docstrings to document functions. A docstring is a multiline string enclosed within triple quotes 
         placed directly below the function definition. A clear docstring to describe its purpose, parameters, return value, and exceptions:
            1. Purpose of the function
            2. Parameters of the function
            3. Return value
            4. Exceptions Raises
      """)
def calculate_area(length, width):
      
      """
        Calculate the area of a rectagle

        Paramters:
        length(float): The length of the rectangle
        width(float): The width of the rectangle

        Returns:
        float: The calculated area of the rectangle
      """
    
 # Validating inputs (e.g. non numerical values or blanks)   
      try:
            length = float(length)
            width = float(width)
      except ValueError:
        raise ValueError("Length and Width must be valid numbers. ")

# Validate inputs (e.g., non-negative values)
      if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
      
      return length * width
print ("Area of a rectangle calculate_area(length=3, width=4) : ", calculate_area(3,4))
          
print("############################################################################################################\n")