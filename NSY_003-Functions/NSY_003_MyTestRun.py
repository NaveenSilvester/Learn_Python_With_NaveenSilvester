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
    ans = print (f"sum of {x} and {y} is: {x + y}")
    return (ans)

add(5,15)

print ("##########################################################################")
def multiply (x, y):
    ans = print (f"Product of {x} and {y} is: {x * y}")
    return (ans)

multiply(5,3)

print ("##########################################################################")
def division(x,y):
    ans = print (f"Division of {x} by {y} is: {x/y}")
    return (ans)

division(12,6)

print ("##########################################################################")
def sub(x,y):
    ans = print (f"Subraction of {x} - {y} is: {x - y}")
    return (ans)


print ("##########################################################################")
def factorial (n):
    p = ""
    for i in range(1, n+1):
        #print (i)
        if i == 1:
            p = 1
        else:
            p = p * (i)
    ans = print (f"Factorial of {n}! is {p}")
    return (ans)

def menu():
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
    elif option == "2":
        a, b = map(int, input("Enter two numbers to subtract (separated by space): ").split())
        sub(a, b)
    
    elif option == "3":
        a, b = map(int, input("Enter two numbers to multiply (separated by space): ").split())
        multiply(a, b)
    elif option == "4":
        a, b = map(int, input("Enter two numbers to divide (separated by space): ").split())
        division(a, b)
    elif option == "5":
        a = int(input("Enter a numbers for determining its factorial: "))
        factorial(a)

    else:
        print("Thank you!")
        exit()

menu()
print ("##########################################################################")
