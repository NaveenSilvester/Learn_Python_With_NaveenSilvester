##################################################################################################
#### Decorator
#### Decorators in Python are a powerful and elegant way to extend or modify the behavior of 
#### functions or methods without permanently changing them. A decorator is essentially a function 
#### that takes another function as input and returns a modified or enhanced version of that function.
##################################################################################################

""""
Decorators in Python are a powerful and elegant way to extend or modify the behavior of functions or 
methods without permanently changing them. A decorator is essentially a function that takes another 
function as input and returns a modified or enhanced version of that function.

How Decorators Work
Decorators are applied using the @decorator_name syntax, placed above the function definition. 
They are useful for tasks like logging, authentication, modifying output, etc.

"""
print("\n############### Example-1: Simple Decorator Function ###########################")
def simple_logger(func):
    def wrapper():
        print(f"Calling Function {func.__name__}")
        return func()
    return wrapper

@simple_logger
def greet():
    print("Hello World")
greet()
print("##################################################################################\n")


print("\n############### Example-2: Decorator Function #################################")
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print (f"Function called {func.__name__} completed in {end_time - start_time} seconds")
        return result
    return wrapper


@timer
def compute_sum(n):
        return sum(range(n))
#compute_sum(1000)
print (compute_sum(100000))
print("##################################################################################\n")


print("\n############### Example-3: Decorator Function (Authentication Example) ##########")

def authenticate (user_role):
     def decorator(func):
          def wrapper(*args, **kwargs):
               if user_role == "Admin":
                    print(f"Access granted to {user_role}")
                    return func(*args, **kwargs)
               else:
                    print (f"Access Denied for {user_role}")
                    return None
          return wrapper
     return decorator

@authenticate(user_role="Admin")
def view_sensitive_data():
     print("Here is Sensitive Data")

@authenticate(user_role="Guest")
def view_sensitive_guest():
     print("Here is Sensitive Data")


view_sensitive_data()
view_sensitive_guest()