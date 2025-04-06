#####################################################################################################################
### Functions - Error Handling
#####################################################################################################################
"""
Error Handling
In Python, error handling is primarily managed using try, except, else and finally blocks. This mechanism allows you to anticipate and handle exceptions – unexpected events or errors that occur during program execution – without crashing your program.
Here’s a breakdown
try-except
The try block is used to write code that may raise an exception. If an exception occurs, the corresponding except block handles it.
try:
	num = int(input(“Enter a number : “))
	print(10/num) # Risk of ZeroDivisionError
except ZeroDivisionError:
	print(“You cannot divide by Zero!”)
except ValueError:
	print(“Invalid Input: Please enter a Number”)
else
	The else block is executed only if no exceptions are raised in the try block.
try:
	num = int(input(“Enter a number : “))
	print(10/num) # Risk of ZeroDivisionError
except ZeroDivisionError:
	print(“You cannot divide by Zero!”)
except ValueError:
	print(“Invalid Input: Please enter a Number”)
else:
	print(“Input processed successfully”)

finally
	The finally block is used to write code that should execute no matter what – whether an exception occurs or not. This is useful for cleanup actions (e.g., closing files or releasing resources)
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File operation completed.")
Key Points:
•	Exceptions are represented by specific error types like TypeError, ValueError, and ZeroDivisionError.
•	You can raise your own exceptions using the raise statement
•	Custom exception can be defined using classes that inherit from Python’s Exception class

Examples:
	Example-1: Handling Multiple Exceptions
	def process_input(data):
    try:
        number = int(data)
        print(f"Square of the number is: {number**2}")
    except ValueError:
        print("Error: Input is not a valid integer!")
    except TypeError:
        print("Error: Input type is not supported!")

# Testing
process_input("5")  # Valid input
process_input("abc")  # ValueError
process_input(None)  # TypeError
	Example-2: Catching all Exceptions
	Sometimes, you may not know the specific error type, so you can use a generic exception handler.
def divide(a, b):
    try:
        result = a / b
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    else:
        return result

# Testing
print(divide(10, 2))  # Works fine
print(divide(10, 0))  # ZeroDivisionError
print(divide(10, "x"))  # TypeError
	Example-3: Using Custom Message
Add custom messages to exceptions for clarity.
try:
    raise ValueError("This is a custom error message!")
except ValueError as e:
    print(f"Caught an exception: {e}")

Example-4: Using Finally for Cleanup
When working with resources like files or databases, use finally to ensure cleanup.
def read_file(file_name):
    try:
        file = open(file_name, "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found!")
    finally:
        print("Closing the file.")
        file.close()

# Testing
read_file("example.txt")

Example-5: Functions with built-in error handling
def safe_cast(value, target_type):
    try:
        return target_type(value)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None

# Testing
print(safe_cast("123", int))  # Converts to 123
print(safe_cast("abc", int))  # Fails and handles the error

"""

###############################################################################
### Functions - Error Handling
###############################################################################
print("\n#################################################################################")
print ("################### Example-1 ###################################################")
print ("The else block is executed only if no exceptions are raised in the try block.")
try:
    num  = int(input("Enter a number: \n", ))
    res = 10/num
except ZeroDivisionError:
    print ("The number cannot be Zero")
except ValueError:
    print ("Non numeric characters not allowed")
else:
    print (f"The result of dividing 10 by {num} is {res}") 

print ("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-2 ###################################################")
print ("The else block is executed only if no exceptions are raised in the try block.")
print ("The finally block is used to write code that should execute no matter what  whether an exception occurs or not. This is useful for cleanup actions (e.g., closing files or releasing resources)")
try:
    num  = int(input("Enter a number: \n", ))
    res = 10/num
except ZeroDivisionError:
    print ("The number cannot be Zero")
except ValueError:
    print ("Non numeric characters not allowed")
else:
    print (f"The result of dividing 10 by {num} is {res}") 
finally:
    print ("This is the final Message")
print ("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-3 ###################################################")
print ("The else block is executed only if no exceptions are raised in the try block.")
print ("The finally block is used to write code that should execute no matter what  whether an exception occurs or not. This is useful for cleanup actions (e.g., closing files or releasing resources)")

def greet(x):
    try:
        if x == "":
            raise ValueError("Please Enter an Argument")
    except ValueError as e:
        return (e)
    else:
        return (f"Hello {x} welome to the World Of Python Programming!")
print("Calling the Function greet('') : ", greet(""))    
print("Calling the Function greet('Allen') : ", greet("Allen"))    
print ("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-4 ###################################################")
print ("The else block is executed only if no exceptions are raised in the try block.")
print ("The finally block is used to write code that should execute no matter what  whether an exception occurs or not. This is useful for cleanup actions (e.g., closing files or releasing resources)")

def age_category(x):
    try:
        if x < 0:
            raise ValueError ("Age should be more than 0")
        if x == "":
            raise ValueError ("Please Enter an Valide Number")
    except ValueError as e:
        return (e)            
    else:
        if x > 0 and x < 18:
           return ("You are Minor\n")
        elif x > 17 and x <= 25:
           return ("You are young man\n")
        elif x > 25 and x <= 50:
           return  ("Middle Aged man\n")
        else:
           return ("Senior Citizen")

print("Calling the Function age_category(-1) : ", age_category(-1))    
print("Calling the Function age_category(1) : ", age_category(1))
print("Calling the Function age_category(12) : ", age_category(12))
print("Calling the Function age_category(26) : ", age_category(26))
print("Calling the Function age_category(48) : ", age_category(48))
print("Calling the Function age_category(51) : ", age_category(51))           
