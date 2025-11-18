#####################################################################################################################
## Dictionary Data Type
#####################################################################################################################
"""
Dictionary (dict):
•	A dictionary maps key to values. Each key is unique and immutable, while the values can be of any data type and are not required to be unique.
•	Dictionaries are mutable, meaning you can add, remove, or update key-value pairs
Creation of Dictionary
Dictionaries can be created using curly braces {} or the dict() constructor:
Example: 
	# Using Curly Braces
my_dict = {‘name’: ‘Alice’, ‘age’ : 23,  ‘Place’: ‘Bangalore’}
# Using dict contructor
my_dict = dict(name=”Bob”, Age=23)
Accessing Element
	You can access values in a dictionary by their keys:
	print (my_dict[‘name’]) # output: Bob
	Alternatively you can use get() method to avoid errors if a key does not exist
	print(my_dict.get(‘age’)) # Output: 23
	print(mydict.get(‘name’,’age’,’place’) # Output: Alice, 23, Bangalore

Updating Dictionary
You can add, update or remove key-value pairs
# Adding a new key-value pair
my_dict[‘country’] = ‘India’
# Updating an existing key
my_dict['name’] = ‘Allen’
# Removing key-value pair
del my_dict[‘country’]
Common dictionary Methods
1.	keys(): Returns a view object of all keys in the dictionary
my_dict = {"name": "Bob", "age": 30}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

2.	values(): Returns a view object of all values
print(my_dict.values()) # Output: dict_values[”Bob”, 30]

3.	items(): Returns a view object of key-value pairs
4.	update(): Updates the dictionary with another dictionary or iterable of key-value pair
5.	clear(): Removes all elements in the dictionary
6.	copy(): creates a shallow copy of dictionary

Key Features
•	Keys are case-sensitive (‘Name’ and ‘name’ are different)
•	Unordered, Dictionaries are unordered
•	Dictionaries are mutable, meaning you can change, add, or remove key-value pairs after creation.
•	Keys must be unique and immutable (e.g., strings, numbers or tuples)
•	Values can be of any data type
•	Dictionary is defined using {}

Common Methods
.keys(): Returns all keys in the dictionary
	My_dict.keys() -> [‘name’, ‘age’]
.values(): Returns all values in the dictionary
	My_dict.values() - > [‘Alice’, 23]
.items(): Returns key-value pairs as tuples
	My_dict.items() -> [(‘name’ ,’Alice’, ‘age’,23)]
.pop(key): Removes a key and returns its value
	My_dict.pop(‘age’) -> 23
.update(other_dict): Updates the dictionary with another 
		My_dict.update(‘Country’: ‘USA’) 


Performance consideration while using Dictionaries:
Dictionaries in Python are highly optimized for key-value lookups but come with their own performance considerations. Here is what you need to keep in mind:
1.	Time Complexity of Operations
Accessing Values: Retrieving a value by its key is O(1) on average due to the underlying hash table implementation
Adding or updating elements: These operations are also O(1) on average.
Deleting Elements: Deleting a specific key-value pair is O(1), while clearing the dictionary using clear() is O(n)
However, in the worst case (hash collisions), these operations can degrade to O(n)
2.	Memory Usage
Dictionaries can consume significant memory because of the underlying hash table.
If memory efficiency is a concern, alternatives like collections.Counter (for counting) or defaultdict can sometimes offer optimized use cases.
3.	Hash Collisions
Performance can degrade if there are many hash collisions, where multiple keys map to the same hash bucket.
Using keys with a good distribution in their hash function (e.g., integers or strings) reduces the risk of collisions.
4.	Iterations Costs
Iterating over a dictionary using methods like items(), keys(), or values() is O(n), where n is the number of items in the dictionary.
Iteration can be memory-efficient, but copying large dictionaries can be expensive.
5.	Dynamic Resizing
Python dictionaries dynamically resize themselves when the number of elements grows.
Resizing is computationally expensive, so preallocating dictionary size (if possible) can help in performance-critical applications
6.	Immutability of Keys
Only hashable (immutable) data types like strings, numbers, or tuples can be used as keys. Using mutable keys, such as lists, will throw an error
7.	Optimization for Membership Checks
Checking if a key exists using the “in” keyword is O(1) on average.
8.	Alternatives for specialized use cases
For highly memory-intensive applications, consider using alternatives like:
-	collections.defaultdict: automatically provides default values for missing keys
-	collections.OrderedDict: Preserves the order of insertion (through standard dictionaries also do so from Python 3.7+)
-	collections.Counter: Ideal for counting elements
-	set: for scenarios focused purely on membership testing. 

Examples of how to use Dictionaries in Python
Example-1: Mapping Values:
Dictionaries are commonly used for mapping unique key to values
students_scores = {“Allen”: 100, “Alice”: 95, “Bob”: 85}
print(students_scores[“Allen”]) #Output: 100
Example-2: Counting Occurrences
Dictionaries can be used to count occurrences of items in a list or a sequence
fruits = [“apple”, “banana”, “orange”, “apple”, “orange”, “apple”, “mango”]
count= {}
for fruit in fruits:
	count[fruit] = count.get(fruit, 0) + 1
print (count) # Output: {“apple” : 3, “banana”: 1, “Orange”:2, “mango”: 1}
Example-3: Updating Values
You can update values dynamically based on some logic
inventory = {“apples”: 100, “oranges” : 80, “bananas”: 50}
# Update Stock
inventory[“apples”] += 20
inventory[“bananas”] -= 10
print (inventory) # Output: {“apples”: 120, “oranges”:80, “bananas”:40}
  Example-4: Dictionary Comprehensions
Create dictionaries efficiently using comprehensions
	squares = { x: x ** 2 for x in range(1,6)}
	print(squares) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Example-5: Fetching API Data
Dictionaries are often used to parse and store JSON data fetched from APIs
import requests
response = requests.get(https://jsonplaceholder.typicode.com/todos/1)
data = response.json() # converted JSON to Python Dictionary
print (data[“Title”] # Output: prints the title from the API response
 

"""
###############################################################################
### Creating a Dictionary
###############################################################################
print("\n#############################################################")
print ("################### Creating a Dictionary ###################")
print ("Dictionary can be created using Curly bracket")
school_record = {
    "Student ID" : "001",
    "Student Name" : "Allen",
    "Class" : "9th",
    "Section" : "C",
	"Score": 90
}
print ("The Dictionary school_record contains the following elements: ", school_record)
print("#######################################################\n")

print("\n##################################################################################")
print ("################### Accessing elements from a Dictionary by key ###################")
print ("Accessing Name of the Student from the Dictionary : ", school_record["Student Name"])
print ("Accessing Key name by using value from the Dictionary : ", school_record.get("Class"))
print("####################################################################################\n")

print("\n#####################################################################################")
print ("################### To Fetch Keys of Dictionary  #####################################")
print ("Keys of dictionary school_record : ", school_record.keys())
print("#######################################################################################\n")

print("\n#####################################################################################")
print ("################### To Fetch Values of Dictionary  #####################################")
print ("Keys of dictionary school_record : ", school_record.values())
print("#######################################################################################\n")

print("\n#####################################################################################")
print ("################### To Fetch Key-Values of Dictionary  ###############################")
print ("Keys of dictionary school_record : ", school_record.items())
print("#######################################################################################\n")

print("\n#############################################################################")
print ("################### Updating Dictionary  #####################################")
print ("The Dictionary school_record contains the following elements: ", school_record)
print ("Update Dictionary by adding a new key-value Country value India")
school_record["Countrty"] = "INDIA"
print ("Updated Dictionary school_record contains the following elements: ", school_record)
print("################################################################################\n")

print("\n#############################################################################")
print ("################### Updating Dynamically the values of Dictionary  ###########")
print ("The Dictionary school_record contains the following elements: ", school_record)
print ("Dynamic Update Dictionary by adding + 10 to  score")
school_record["Score"] += 10
print ("Updated Dictionary school_record contains the following elements: ", school_record)
print("################################################################################\n")

print("\n##########################################################################################")
print ("################### Counting occurencey of elements in a list using Dictionary  ###########")
fruit_basket = ["apple","banana", "orange", "fig", "apple", "orange", "apple", "fig"]

count = {} # declaring a dictionary

for fruit in fruit_basket:
	count[fruit] = count.get(fruit, 0) + 1

print ("Counts of Fruit in Fruit Basket : ", count)
print("##########################################################################################\n")

print("\n#######################################################")
print ("################### Dictionary Comprehension ###########")
squares = {x:x**2 for x in range(10)}
print ("Dictionary of Squares : ", squares)
print("#######################################################\n")


""""
print("\n#######################################################################################")
print ("################### Fetching API data (JSON) and converting it to Dictionary ###########")
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
for post in data:
	print("\n#################################################")
	print("UserId : ", post["userId"])
	print("ID : ", post["id"])
	#print("ID: ", post["id"])
	print("Title: ", post["title"])
	print("Body: ", post["body"])
	print("#################################################\n")
print("#######################################################################################\n")
"""
#names = ["Allen", "Maria", "Allen", "Silvester", "Maria", "Allen"]
sentence ="How are you? How is life?"
words = sentence.split(sep=" ")
print (list)

count={}
for word in words:
	count[word] = count.get(word, 0) + 1

print (count)