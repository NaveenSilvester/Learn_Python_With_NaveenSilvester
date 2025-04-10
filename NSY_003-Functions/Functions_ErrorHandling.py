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



Common built-in exceptions
1.	ValueError
Occurs when an operation or function receives an argument of the correct type but an in appropriate value.
try:
	number = int(“abc”) # Invalid value for integration conversion
except ValueError as e:
	print(f”ValueError: {e}”)

2.	TypeError
Occurs when an operation or function is applied to an object of inappropriate type.
try:
	result = “2”  + 3 # Adding a string to an integer
except TypeError as e:
	print(f“TypeError: {e}”)

3.	ZeroDivisionError
Occurs when division or module by zero is attempted
try:
	result = 100/0
except ZeroDivisionError as e:
	print(f”ZeroDivisionError : {e}”)

4.	IndexError
Occurs when attempting to access an invalid index in a sequence (e.g., list or string)
try:
	my_list = [1,2,3]
	print([my_list[5]) # Invalid Index
except IndexError as e:
	print(f”IndexError: {e}”)

5.	KeyError
Occurs when a dictionary key that doesn’t exist is accessed.
try:
	my_dict = {“name”: “Allen”}
	print(my_dict[“age”]) # Non-existent key
except KeyError as e:
	print(f”KeyError: {e}”)

6.	AttributeError
Occurs when an invalid attribute is accessed or an assignment is attempted on an object
try:
	num = 5
	num.append(6) # Integers don’t have an ‘append’ method
except AttributeError as e:
	print(f”AttributeError: {e}”)

7.	FileNotFoundError
Occurs when trying to access or open a file that does not exist
try:
	with open(“nonexistent_file.txt”, “r”) as file:
		content = file.read()
except FileNotFoundError as e:
	print(f”FileNotFoundError: {e}”)

8.	ImportError
Occurs when an import statement fails to find the specified module or cannot load it.
try:
	import nonexistent_module # Non-existent module
except ImportError as e:
	print(f“ImportError: {e}”)

9.	RuntimeError
Occurs when an error is detected that does’nt fal into any specific category
try:
	raise RunTimeError(“This is a custom runtime error.”)
except RunTimeError as e:
	print(f”RunTimeError: {e}”)

10.	StopIteration
try:
	my_iter = iter([1,2,3])
	while True:
		print(next(my_iter)) # Keep calling ‘next’ until exhausted
except StopIteration as e:
	print(f“StopIteration: {e}”)

11.	AssertionError
Raised when an assert statement fails
try:
	x = 10
	assert x < 5, “value should be less than 5”
except AssertionError as e:
	print(f”AssertionError : {e}”)

12.	NameError
Occurs when a variable or function name that hasn’t been defined is accessed.
try:
	print(undefined_variable) # Variable is not defined
except NameError as e:
	print(f”NameError: {e}”)

13.	EOFError
Occurs when the input() function reaches the end of a file (EOF) and no more data is available.
try:
	user_input = input(“Enter something: “) # Trigger with end-of-file
except EOFError as e:
	print(f”EOFError: {e}”)


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
    finally:
        print ("Program is Completed its run!")

print("Calling the Function age_category(-1) : ", age_category(-1))    
print("Calling the Function age_category(1) : ", age_category(1))
print("Calling the Function age_category(12) : ", age_category(12))
print("Calling the Function age_category(26) : ", age_category(26))
print("Calling the Function age_category(48) : ", age_category(48))
print("Calling the Function age_category(51) : ", age_category(51))   




print("\n#################################################################################")
print ("################### Example-5 (ValueError) ######################################")
try:
	number = int("abc") # Invalid value for integration conversion
except ValueError as e:
	print(f"ValueError: {e}")
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-6 (TypeError) #######################################")
try:
	result = "2" + 3 # Adding a string to an integer
except TypeError as e:
	print(f"TypeError: {e}")
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-7 (ZeroDivisionError) ###############################")
try:
	result = 20 / 0 # Dividing by Zero
except ZeroDivisionError as e:
	print(f"ZeroDivisionError: {e}")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-8 (IndexError) ###############################")
try:
    my_list = [1,2,3]
    print(my_list[4]) # Invalid Index
except IndexError as e:
	print(f"IndexError: {e}")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-9 (KeyError) ###############################")
try:
    my_dict = {"name": "Allen"}
    print(my_dict["age"]) # Invalid key
except KeyError as e:
	print(f"KeyError: {e}")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-10 (AttributeError) ###############################")
try:
    num = 5
    num.append(6) # Invalid method
except AttributeError as e:
	print(f"AttributeError: {e}")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-11 (FileNotFoundError) ###############################")
try:
    with open("Myfile.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
	print(f"FileNotFoundError: {e}")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-12 (ImportError) ####################################")
try:
    import jn # Non Existing module
except ImportError as e:
	print(f"ImportError: {e}")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-13 (StopIteration) #############################")
try:
    my_iter = iter([1,2,3])
    while (True):
        print(next(my_iter)) # Keep calling "next" unitl exhausted
except StopIteration as e:
	print(f"StopIteration: {e}")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-13 (AssertionError) #############################")
try:
    x = 10
    assert x < 5, "value should be less than 5"
except AssertionError as e:
	print(f"AssertionError: {e}")
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-14 (NameError) #############################")
try:
    x = 10
    print(f"Value of x is {y}")
except NameError as e:
	print(f"NameError: {e}")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-15 (EOFError) #############################")
try:
    user_input = input("Enter your name")
except EOFError as e:
	print(f"EOFError: {e}")
print("#################################################################################\n")