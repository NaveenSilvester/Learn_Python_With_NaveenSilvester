#####################################################################################################################
## Tuple Data Type
#####################################################################################################################
"""
A tuple in Python is an immutable, ordered collection of items. Unlike lists, tuples cannot be modified after creation, making them ideal for storing data that should remain constant. Here is a breakdown of its characteristics.
1.	Immutable:
Similar to lists, but immutable – values cannot be altered after creation
Useful for storing fixed data
Example: t = (1, “two”, 3/0)
2.	Ordered:
Tuples maintain the order of elements, meaning you can access items using their index.
3.	Defined Using Parenthesis:
A tuple is created using parentheses () or the tuple() function.
Example:
My_tuple = (1, “Hello”, 3.14)
4.	Flexible Data Types:
Tuples can contain elements of different data types: Integers, strings, floats other tuples etc.,
5.	Unpacking:
You can unpack tuple elements directly into variables
a, b, c = my_tuple
6.	Memory Efficiency:
Tuples often require less memory than lists because they are immutable
Common Features:
All sequence types support slicing and indexing to access individual items or ranges of items. 
You can iterate over sequences using loops
Example: l = [1,2,3,4]
	     Print(l[1:3])  # output [2,3]

Examples of Tuples
1.	Creating a Tuple
# A tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, True)

# A tuple containing another tuple
nested_tuple = (1, 2, (3, 4))
2.	Accessing Elements
# Accessing elements by index
print(mixed_tuple[1])  # Output: Hello

# Negative indexing
print(mixed_tuple[-1])  # Output: True

3.	Tuple Operations
# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2  # Output: (1, 2, 3, 4)

# Repeating
repeated_tuple = ("Hi",) * 3  # Output: ('Hi', 'Hi', 'Hi')

4.	Unpacking Tuples:
# Unpacking into variables
x, y, z = (5, 10, 15)
print(x, y, z)  # Output: 5 10 15

5.	Tuple Methods
# Count and index methods
sample_tuple = (1, 2, 3, 2, 2)
print(sample_tuple.count(2))  # Output: 3
print(sample_tuple.index(3))  # Output: 2

6.	Tuples as Function Returns
# Example function
def calculate(x, y):
    return x + y, x * y

sum_result, product_result = calculate(3, 5)
print(sum_result, product_result)  # Output: 8 15

7.	Immutable Nature
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 10  # Uncommenting this line will raise an error

8.	Tuple for Data Integrity
coordinates = (45.0, 92.0)  # Immutable latitude and longitude values
print(f"Coordinates: {coordinates}")

"""


###############################################################################
### Creating a Tuple
###############################################################################
print("\n#######################################################")
print ("################### Creating a Tuple ###################")
print ("Tuples can be created using parenthesis or tuple() function")
print("Ensure that you add a trailing comma if you are creating a single element tuple")
my_tuple = (1,"Hello", 3.14, (100,200,300,400))
print("My Tuple contains: ", my_tuple)
single_element_tuple = (100,)
print("Single Element Tuple single_element_tuple contains : ", single_element_tuple)
print("#######################################################\n")


print("\n#######################################################")
print ("################### Accessing a Tuple ###################")
mixed_tuple = (1, "Hello", 3.14, True)
print ("Accessing 2nd element in tuple mixed_tuple[1]: ", mixed_tuple[1])
print("#######################################################\n")

print("\n#######################################################")
print ("################### Concatenating two Tuple ###################")
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print ("Tuple1 has (1,2), Tuple2 has (3,4), concatenating them together to a new tuple Result gives: ", result)
print("#######################################################\n")


print("\n#######################################################")
print ("################### Unpacking Tuples to Variables ###################")
mixed_tuple = (1, "Hello", 3.14, True)
a, b, c, d = mixed_tuple
print ("mixed_tuple contains elements mixed_tuple = (1, \"Hello\", 3.14, True), on unpacking we get : ", a, b, c, d)
print("#######################################################\n")

print("\n#######################################################")
print ("################### Count and Index methods in Tuples ###################")
mixed_tuple = (1, "Hello", 3.14, True)
print ("Count method fetches the index of the specified element from the tuple: ", mixed_tuple.count("Hello"))
print ("Get the index of the element based on the value: ", mixed_tuple.index(3.14))
print("#######################################################\n")


print("\n#######################################################")
print ("################### Tuples as Function Returns ###################")
def calcualte(x,y):
    return x+y, x*y

print ("Sum and Product of (2,3) are: ", calcualte(2,3))
print("#######################################################\n")

print("\n#######################################################")
print ("################### Zip function ###################")
names = ("Allen", "Lambert", "Kane")
section = ("C", "B", "A")
Zipped = zip(names,section)
print ("Zipped elements as tuples : ", list(Zipped))
print("#######################################################\n")



print("\n#######################################################")
print ("################### Iterations in Tuples ###################")
data = (("Alice", 25), ("Bob", 30), ("Charlie", 35))
for name, age in data:
    print (f"Name is {name} is {age} years old \n")
print("#######################################################\n")