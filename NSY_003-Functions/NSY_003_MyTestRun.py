print("------------------------------------------------------------------------------------------------------")
print ("FUNCTIONS IN PYTHON")
print("------------------------------------------------------------------------------------------------------")

print ("##########################################################################")

def greet():
    print ("Hi Greeting to you!")
greet()

print ("##########################################################################")
def greet_by_name(var):
    print (f"Welcome {var}")

greet_by_name("Joseph")

print ("##########################################################################")

def add(x,y):
    """
    The function adds to integers and throws the result
    Parameters: Two integers separated by a space
    Returns: Print statement of results
    Raises:
        ValueError: If the Input is empty
    """
    if x is None or y is None:
        raise ValueError("The list of numbers cannot be empty.")
    
    return (x + y)



print ("##########################################################################")
def multiply (x=None, y=None):
    """
        Description: This function finds product to two integers.
        Paramerters: x (int) : First Integer
                     y (int) : Second Integer
        Returns:
            int: Product of x and y
        
        Raises:
            ValueError: If either input is None 

    """
    #ans = print (f"Product of {x} and {y} is: {x * y}")
    if x is None or y is None:
        raise ValueError("Inputs cannot be None")
    return (x * y)
    

print ("##########################################################################")
def division(x=None,y=None):
    """
        Description: This function finds division of two integers.
        Paramerters: x (int) : First Integer
                     y (int) : Second Integer
        Returns:
            int: Division of x and y
        
        Raises:
            ValueError: If either input is None 

    """
    if x is None or y is None:
        raise ValueError("Inputs cannot be None")

    return (x / y)


print ("##########################################################################")
def sub(x=None,y=None):
    """
        Description: This function finds Subtraction to two integers.
        Paramerters: x (int) : First Integer
                     y (int) : Second Integer
        Returns:
            int: Subtracting x from y
        
        Raises:
            ValueError: If either input is None 

    """
    if x is None or y is None:
        raise ValueError("Inputs cannot be None")

    return (x - y)


print ("##########################################################################")
def factorial (x=None):
    """
        Description: This function finds factorial of an integer.
        Paramerters: x (int) : First Integer
        Returns:
            int: Factorial of x
        
        Raises:
            ValueError: If either input is None 

    """
    if x is None:
        ValueError("Input cannot be None")
    p = ""
    for i in range(1, x+1):
        #print (i)
        if i == 1:
            p = 1
        else:
            p = p * (i)
    return (p)


def menu():
    """
        Displays an interactive menu for basic arithmetic operations and executes 
        the corresponding function based on user selection.

        The menu provides the following options:
            1. Addition of two integers
            2. Subtraction of two integers
            3. Multiplication of two integers
            4. Division of two integers
            5. Factorial of a single integer

        Behavior:
            - Prompts the user to select an option from the menu.
            - Requests the required input(s) depending on the chosen operation.
            - Calls the appropriate helper function (add, sub, multiply, division, factorial).
            - Prints the result of the operation to the console.
            - Exits gracefully if the user enters an invalid option.

        Parameters:
            None (all inputs are taken interactively from the user).

        Returns:
            None (results are printed directly to the console).

        Raises:
            ValueError: If the user enters non-integer values where integers are expected.
            ZeroDivisionError: If division by zero is attempted.
        """
    option = input("""Select the functionality: 
              1. Add
              2. Subtract      
              3. Product
              4. Division
              5. Factorial       
           """)
    

    if option == "1":
        a, b = map(int, input("Enter two numbers to add (separated by space): ").split())
        add(a, b)
        print (f"Sum of {a} and {b} is: {add(a,b)}")
    elif option == "2":
        a, b = map(int, input("Enter two numbers to subtract (separated by space): ").split())
        print (f"Subtraction of {a} - {b} is: {sub(a, b)}")
    
    elif option == "3":
        a, b = map(int, input("Enter two numbers to multiply (separated by space): ").split())
        print (f"Product of {a} and {b} is: {multiply(a,b)}")

    elif option == "4":
        a, b = map(int, input("Enter two numbers to divide (separated by space): ").split())
        print (f"Division of {a} by {b} is: {division(a, b)}")

    elif option == "5":
        a = int(input("Enter a numbers for determining its factorial: "))
        print (f"Factorial of {a}! is: {factorial(a)}")

    else:
        print("Thank you!")
        exit()

menu()
print ("##########################################################################")

print("------------------------------------------------------------------------------------------------------")
print ("GENERATORS IN PYTHON")
print("------------------------------------------------------------------------------------------------------")
numbers_g = (x for x in range(1000000))
numbers_list = list(numbers_g)
print(numbers_list[:10])


print("------------------------------------------------------------------------------------------------------")
print ("Lambda function IN PYTHON")
print("------------------------------------------------------------------------------------------------------")
square = lambda x : x ** 2
print (square(5))


cube = lambda x : x**3
print (cube(3))

area_of_square = lambda l,b : l * b
print (f"AREA of SQUARE {area_of_square(2,4)}")

area_of_circle = lambda r : 1.34 * r
print (f"Area of Circle {area_of_circle(3)}")

numbers = [1,2,3,4,5,6,7,8]
a = list(filter( lambda x : x %2 == 0, numbers))
print (a)

print ("#################################################################")
numbers = [5, 12, 17, 18, 24, 32]
print(list(filter(lambda x : x%2 == 0, numbers)))


print ("#################################################################")

fruits = ["apple", "banana", "avocado", "cherry", "apricot"]
def getbyletter(c, list):
    mylist = []
    for item in list:
        if item.startswith(c):
            mylist.append(item)
    return mylist

g = getbyletter("a",fruits)
print (g)
print ("#################################################################")


a = [ item for item in fruits if item.startswith("a")]
print (f"HERE is the list {a}")
print ("#################################################################")


al = list(filter(lambda item : item.startswith("a"), fruits ))
print (f"List is {al}")
print ("#################################################################")


numbers = [5, 12, 17, 18, 24, 32]
even = list(filter(lambda x: x%2==0, numbers))
print (f"Even numbers are {even}")
print ("#################################################################")

fruits = ["apple", "banana", "avocado", "cherry", "apricot"]
a = list(filter( lambda x: x.startswith("a"), fruits))
print(f'Fruits starts with "a" are: {a}')
print ("#################################################################")

print("------------------------------------------------------------------------------------------------------")
print ("Try exception IN PYTHON")
print("------------------------------------------------------------------------------------------------------")

try:
    num = int(input("Enter a number: "))
    print(f"The square of the number is {num**2}")
except ValueError:
    print("Error: Please enter a valid integer!")


try:
    num = int(input("Enter a number: "))
    print(f"The Division of the 10 by number is {10/num}")
except ValueError:
    print("Error: Please enter a valid integer!")
except ZeroDivisionError:
    print("Error: Enter a number >0")
else:
    print ("Success!")
finally:
    print ("FINALLY the code")

print ("#################################################################")

celsius = [0,10,20,30]
f = [(c, (c * (9/5) + 32)) for c in celsius ]
print(f)


print("------------------------------------------------------------------------------------------------------")
print ("Recursive function IN PYTHON")
print("------------------------------------------------------------------------------------------------------")

def factorial (n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

print (f"Factorial of 5 is {factorial(5)}")
print ("#################################################################")


print("------------------------------------------------------------------------------------------------------")
print ("Callback function IN PYTHON")
print("------------------------------------------------------------------------------------------------------")
def greet(n):
    return ("Hello" + n)
   

def execute_callback(callbackfunction, *args):
    return callbackfunction(*args)

result = execute_callback(greet, "Naveen")

print(result) 
print ("#################################################################")

words = ["Apple", "Banana", "Fig"]

def sort_by_length(word):
    return len(word)
words = ["Apple", "Banana", "Fig"]
words.sort(key=sort_by_length)
print(words)

print ("DDDDDDDDDDDDDDDDDDDDDDDD")

words = ["Apple", "Banana", "Fig"]
words.sort(reverse=True)
print (words)
print ("#################################################################")
print ("I am at the end of the code")
print ("#################################################################")

import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 15), 20)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -7), -10)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-5, 10), 5)

if __name__ == "__main__":
    unittest.main()



