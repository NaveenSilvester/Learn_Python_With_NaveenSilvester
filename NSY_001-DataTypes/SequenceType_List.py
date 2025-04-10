#####################################################################################################################
## List Data Type
#####################################################################################################################

"""
List (list):
•	A mutable collection that can hold items of various data types
•	Allows insertion, deletion, and modification of elements
•	Example: l = [1, “hundred”, 5.9, “7”]


List (list): 
	In Python, a list is a built-in data type that is used to store collections of items. It is an ordered, mutable (changeable), and heterogenous data structure, meaning it can contain elements of different data types (e.g., integers, strings or even other lists).
	Characteristics of Lists:
•	Ordered: Elements in a list maintain the order in which they are inserted. You can access them using their index.
•	Mutable: A mutable collection that can hold items of various data types. Allows insertion, deletion, and modification of elements
Example: l = [1, “hundred”, 5.9, “7”]
•	Heterogeneous: A single list can contain items of different data types
•	Dynamic Size: Lists in Python can grow or shrink dynamically as elements are added or removed.
•	A List is created by enclosing elements in a square brackets [], separated by commas.
Common List Methods
•	Accessing List Elements:
my_list = [10, 20, 30]
print (my_list[1]) # Output: 20

•	Modifying List Elements:
my_list[1] = 40
print (my_list) # Output: 10, 40, 30

•	Adding List Elements:
o	Append Method append(): Adding element to the end of the list
my_list.append(50)
print(my_list) # Output: 10,40,30, 50

o	Insert Method insert(): Add element at a specific index of list
my_list.insert(1,15)
print(my_list) # 10, 15, 40, 30, 50

o	extend method extend(): Extends the list by appending elements from another iterable (e.g., list or tuple)
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)  # Output: [1, 2, 3, 4]

•	Removing List Elements:
o	Using remove(): To remove or delete an element by its value
my_list.remove(15)
print(my_list) # 10,40,30,50
o	Using pop(): Removes and returns the element at the specified index (default is the last element).
my_list.pop(2)
print(my_list) # Output: 10,40,50
•	Iterate through List:
o	for i in my_list:
                   print (i)
•	 len(list): Gives the length of the list/number of elements in a list
•	sum(list): Calculates the sum of all numeric elements in a list
•	min(list): Returns the smallest element in the list
•	max(list): Return the largest element in the list
•	sorted(list): Returns sorted version of the list (does not modify the original) 
•	index(item[, start[, end]]): Returns the index of the first occurrence of the specified element
my_list = [1, 2, 3]
print(my_list.index(2))  # Output: 1
•	count(item): Returns the number of occurrences of the specified element.
my_list = [1, 2, 2, 3]
print(my_list.count(2))  # Output: 2
•	sort([key[, reverse]]): Sorts the list in place
•	reverse(): Reverses the elements in the list
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]
•	clear(): Removes all elements in the list
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
•	copy(): Returns a shallow copy of a list
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]

The copy() function in Python is used to create a shallow copy of a list. A shallow copy means that a new list is created, but the elements within the list are references to the original objects. If the original list contains mutable objects like other lists or dictionaries, changes to these objects will affect both the original and the copied list.
# Example of shallow copy
original_list = [1, 2, [3, 4]]
copied_list = original_list.copy()

# Modifying the original nested list
original_list[2][0] = 99

print(original_list)  # Output: [1, 2, [99, 4]]
print(copied_list)    # Output: [1, 2, [99, 4]] (nested list is affected)
Deep Copy
import copy

# Example of deep copy
original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

# Modifying the original nested list
original_list[2][0] = 99

print(original_list)      # Output: [1, 2, [99, 4]]
print(deep_copied_list)   # Output: [1, 2, [3, 4]] (nested list is unaffected)


Performance Considerations while using List
1.	Dynamic Sizing: Python lists are dynamic array. When a list’s capacity is exceeded, it is resized (typically doubling its size). This resizing operation can be expensive as it involves copying elements to a new memory location.
2.	Indexing and Slicing: Accessing elements by index or slicing is very fast because lists are implemented as arrays, offering O(1) time complexity for indexing and O9k) for slicing (where k is the size of the slice)
3.	Insertion and Deletion:
a.	At the end of the list, appending is usually O(1), except when resizing is needed.
b.	At the beginning or middle, insertion and deletion can expensive (O(n)) since it requires shifting elements. 
4.	Memory Overhead: Lists consume more memory due to their dynamic nature. They store pointers to objects rather than the objects themselves, and there’s extra space to accommodate future growth.
5.	Iterating: Iterating through a list is O(n) in complexity. However, avoid modifying the list (e.g., adding or removing elements) while iterating, as this can lead to unexpected behavior.
6.	List comprehension & Generators: These are generally faster and more concise than traditional for-loop for creating or transforming lists. For large datasets where you only need to iterate, use generators to save memory.
7.	Choice of Data Structures: If frequent insertions and deletions at arbitrary positions are required, consider using collections.deque instead, as it has better performance for these operations. 
8.	Sorting and Searching: 
a.	Sorting a list is O (nlogn) and can be done using methods like sort() or sorted()
b.	Searching with in or index() is O(n) for an unsorted list. If faster lookups are needed consider set or dict
List Comprehension
List comprehension in Python is a concise and elegant wat to create or transform lists. It allows you to perform operations on items in an iterable (like list, range, or string) and generate a new list in a single line of code. Here’s the breakdown:
Syntax:
[Expression for Item in Iterable if Condition]
-	Expression: What you want to do with each time (e.g., transform it, modify it).
-	Item: The variable representing each element from the iterable.
-	Iterable: The data source you are looping over (e.g., a list, range)
-	Condition (optional): A filter to decide which items are included in the result.

Example:
1.	Squares = [x **2 for x in range(10)]
print(Squares) # Output: [0,1,4,9,16,25,36,49,64,81]
2.	 Evens = [x for x in range(10) if x%2 == 0]
print(Evens) # Output: [0,2,4,6,8]
3.	Words = [“hello”,”world”,”Python”] 
uppercase = [word.upper() for word in Words ] 
print(uppercase) # Output: [“HELLO”, “WORLD”, “PYTHON”]
4.	Creating a 2D matrix (list of lists) and transposing it:
Create a 3 x 3 matrix
matrix = [[1,2,3], [4,5,6], [7,8,9]]
# Transpose Matrix
transpose = [row[i] for row in matrix for i in range(len(matrix[0]))] 
5.	Flattening a Nested List
nested = [[1,2,3,4], [5,6], [7,8,9]]
flattened = [item for sublist in nested for item in sublist]
print(flattened) # Output: [1,2,3,4,5,6,7,8,9]
data = {'a': 1, 'b': 2, 'c': 3}
6.	Dictionary to List Conversion
# List of keys
keys = [key for key in data]
print(keys)  # Output: ['a', 'b', 'c']

# List of values
values = [value for value in data.values()]
print(values)  # Output: [1, 2, 3]

# List of key-value pairs
key_value_pairs = [(key, value) for key, value in data.items()]
print(key_value_pairs)  # Output: [('a', 1), ('b', 2), ('c', 3)]
7.	Prime Numbers with List Comprehension
n = 30
primes = [x for x in range(2, n + 1) if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]
print(primes)
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
8.	Working with Enumerations
words = ["apple", "banana", "cherry"]
# Create a list of tuples with index and word
indexed = [(index, word) for index, word in enumerate(words)]
print(indexed)
# Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
Generator
	A generator is a type of iterable, like a list, but instead of holding all its elements in memory at once, it yields them one at a time, on demand. Generators are defined using functions and the yield keyword
How do Generators Work?
1.	Yield keyword: When a generator function is called, it returns a generator object but doesn’t execute the function. Execution happens when the generator is iterated.
2.	State Preservation: The function “remembers” where it left off after each “yield”, allowing it to resume from the last point when called again.

Creating a Generator
Def generate_numbers()
	For i in range(5):
	 	yeild(i)
# Using Generator
gen = generate_numbers()
for num in gen:
	print(num)
# Output: 0 1 2 3 4
	Explanation: Each call to yield pauses the function and returns a value. The next iteration resumes from the previous point.

Example:
1.	Infinite Sequence:
Def infinite_counter():
 n=0
while True:
	yield n
	n += 1
counter = infinite_counter()
for i in range(5):
      print (next(counter))
# Output: 0 1 2 3 4

2.	Fibonacci Sequence:
def Fibonacci():
        a, b = 0, 1
         while True:
	yield a
	a, b = b, a + b
fib = fibonacci()
for _ in range(5):
      print (next(fib))
# Output: 0 1 1 2 3

3.	File Processing: Read a file line by line without loading the entire file into memory:
def read_file(filename):
	with open (filename, ‘r’) as file:
		for line in file:
			yield line.strip()

for line in read_file(‘example.txt’):
	print(line)


"""


#############################################################################
### Accessing a list
#############################################################################

#############################################################################
## Accessing all the elements of List
#############################################################################

my_list = [10,20,30]
print ("Here is the contents of my_list : ", my_list)

#############################################################################
## Accessing First Element of the list using Index
#############################################################################
print ("Here is the first element of my_list : ", my_list[0])


#############################################################################
## Accessing Last Element of the list using Index
#############################################################################
print ("Here is the first element of my_list : ", my_list[-1])

#############################################################################
## Accessing specific Element of the list using Index
#############################################################################
print ("Here is the Second element of my_list : ", my_list[1])



#############################################################################
### Modifying a list
#############################################################################
my_list = [1,2,4,4,5]
print("Here are the contents of my_list: ", my_list)

#############################################################################
### Modifying 3rd element of the my_list to 3 from the value of 4
#############################################################################
my_list[2] = 3
print("Here are the contents of modified my_list: ", my_list)



print ("\n##############Adding elements to a List################")
print (""".append(): adding a element at the end of the list, 
          .insert(): Adding at the specified index position
          .extend(): Adding a sublist to main list """)
print ("#########################################\n")
#############################################################################
### Adding elements to list
#############################################################################

#############################################################################
### Appending element to list
#############################################################################
my_list.append(6)
print("Appending element '6' to my_list: ", my_list)

#############################################################################
### Inserting element to list at specific position
#############################################################################
my_list.insert(0,0)
print ("Inserting element '0' as the first element of the my_list: ", my_list)

#############################################################################
### Extending list at specific position
#############################################################################
my_second_list = [7,8,9]
print("my_list : ", my_list)
my_list.extend(my_second_list)
print ("Extending my_list with another list: ", my_list)



print ("\n##############Removing elements from List################")
print ("""remove(): By Element value and 
          pop(): By element position""")
print ("#########################################\n")
#############################################################################
### Removing elements to list
#############################################################################

#############################################################################
### Removing elements to list by value
#############################################################################
my_list.append("Hello")
print("Here are the elements from my_list : ", my_list)

my_list.remove("Hello")
print ("Here is the new list after removing Hello: ", my_list)


#############################################################################
### Removes and returns the element at the specified index 
### (default is the last element).
#############################################################################
my_list.pop(0)
print ("Here is the new list after removing the 1st element from my_list: ", my_list)


print ("\n##############Simple List Functions################")
print ("len(), sum(), min(), max()")
print ("#########################################\n")
#############################################################################
### Length of the list
#############################################################################
print ("Length of the list is: ", len(my_list))

#############################################################################
### Sum of the list
#############################################################################
print ("Sum of the list is: ", sum(my_list))

#############################################################################
### Minimum of the list
#############################################################################
print ("Min of the list is: ", min(my_list))

#############################################################################
### Maximum of the list
#############################################################################
print ("Max of the list is: ", max(my_list))

print ("\n##############Sorted List################")
print ("Note: Sorted List does not make changes to the Original List")
print ("#########################################\n")

#############################################################################
### Sorted of the list
### Note: Sorted List does not make changes to the Original List
#############################################################################
my_A = [1,3,2,7,4]
print ("Sorted list my_A (Ascending): ", sorted(my_A))
print ("Note: sorted function does not affect the original my_A")
print (my_A)
print ("Sorted list my_A (Descending): ", sorted(my_A, reverse=True))

print ("\n##############Sort List################")
print ("Note: Sort List changes to the Original List")
print ("#########################################\n")
#############################################################################
### Sort the list
### Note: Sort List changes to the Original List
#############################################################################
my_A = [1,3,2,7,4]
my_A.sort()
print ("Sort the list my_A.list(): ", my_A)
my_A.sort(reverse=True)
print ("Sort the list my_A.list(): ", my_A)


#############################################################################
### List Comprehension
#############################################################################
print ("\n##############List Comprehension################")
#Simple List Comprehension
even = [x for x in range(10) if x%2 == 0]
print (f"Even numbers {even}")

squares = [x **2 for x in range(10)]
print (f"Squares are: {squares}")

# Transpose Matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Matrix is : ", matrix)
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))] 
print ("Transpose: ",transpose)

# Flatten Matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Matrix is : ", matrix)
flattenMatrix = [i for row in matrix for i in row]
print ("Flatten Matrix is : ", flattenMatrix)


#############################################################################
### Generators
#############################################################################
print ("\n##############Generators################")
def generate_numbers():
    for i in range(5):
        yield (i)

gen = generate_numbers()
for num in gen:
    print (num)
