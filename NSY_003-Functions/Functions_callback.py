#####################################################################################################################
### Functions - Callback Functions in Python
#####################################################################################################################
"""

"""

print("\n#################################################################################")
print ("################### Example-1 (Simple Callback) #################################")
print("""
Callback functions in Python are functions that are passed as arguments to other functions, 
      to be called (or "called back") at a later time. They are often used for asynchronous 
      programming, event handling, or customization of behavior.
      """)
def greet(x):
    print(f"Hello {x}, Welcome to the world of callback functions!")
def execute_callback(callbackfunction,*args):
    callbackfunction(*args)

print(execute_callback(greet,"NAVEEN"))
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-2 (Simple Callback) #################################")
print("""
Callback functions in Python are functions that are passed as arguments to other functions, 
      to be called (or "called back") at a later time. They are often used for asynchronous 
      programming, event handling, or customization of behavior.
      """)

def greet(x):
    print(f"Hello {x}, Welcome to the world of callback functions!")

def Add(*args):
    T = sum(*args)
    print("Sums is : ", T)
def execute_callback(callbackfunction,*args):
    callbackfunction(*args)

print(execute_callback(greet,"NAVEEN"))
print(execute_callback(Add,(1,2,3)))
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-3 (Simple Callback) #################################")
print("""
Callback functions in Python are functions that are passed as arguments to other functions, 
      to be called (or "called back") at a later time. They are often used for asynchronous 
      programming, event handling, or customization of behavior.
      """)

def execute_callback(callbackfunction,*args):
    callbackfunction(*args)

def findtype(x):
    print("DataType is : ", type(x))

def findlength(x):
    print("Length is ", len(x))

print(execute_callback(findtype,"NAVEEN"))
print(execute_callback(findlength,"NAVEEN"))
print(execute_callback(findtype,[1,2,3,4]))
print(execute_callback(findlength,[1,2,3,4]))

print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-3 (Callback) ########################################")
print("""
Callback functions in Python are functions that are passed as arguments to other functions, 
      to be called (or "called back") at a later time. They are often used for asynchronous 
      programming, event handling, or customization of behavior.
      """)

def sort_by_length(word):
    return len(word)
words = ["Apple", "Banana", "Fig"]

words.sort(key=sort_by_length)
print(words)
print("#################################################################################\n")