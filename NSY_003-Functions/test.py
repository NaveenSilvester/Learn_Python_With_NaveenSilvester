numbers = [5, 12, 17, 18, 24, 32]
print(list(filter(lambda x : x%2 == 0, numbers)))


fruits = ["apple", "banana", "avocado", "cherry", "apricot"]
def getbyletter(c, list):
    mylist = []
    for item in list:
        if item.startswith(c):
            mylist.append(item)
    return mylist

g = getbyletter("a",fruits)
print (g)

a = [ item for item in fruits if item.startswith("a")]
print (f"HERE is the list {a}")

al = list(filter(lambda item : item.startswith("a"), fruits ))
print (f"List is {al}")

numbers = [5, 12, 17, 18, 24, 32]
even = list(filter(lambda x: x%2==0, numbers))
print (f"Even numbers are {even}")

fruits = ["apple", "banana", "avocado", "cherry", "apricot"]
a = list(filter( lambda x: x.startswith("a"), fruits))
print(f'Fruits starts with "a" are: {a}')


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


celsius = [0,10,20,30]
f = [(c, (c * (9/5) + 32)) for c in celsius ]
print(f)

def factorial (n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))

print (f"Factorial of 5 is {factorial(5)}")


def greet(n):
    return ("Hello" + n)
   

def execute_callback(callbackfunction, *args):
    return callbackfunction(*args)

result = execute_callback(greet, "Naveen")

print(result) 


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