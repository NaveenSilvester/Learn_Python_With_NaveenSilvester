#####################################################################################################################
## Set Data Type
#####################################################################################################################
"""
	Set
	In Python, the set data type is an unordered collection of unique elements. It is useful for storing and performing operations on items without duplicates. Here is an explanation of the key features, operations and use case of sets:
Key Features of a Set:
1.	Unordered:
Sets do not maintain any specific order of elements
my_set = {1,3,0,2}
print(my_set) # Output : {1,2,3,0}
2.	Unique Elements:
Sets automatically removes duplicate values
my_set = {1, 2,3,1,0}
print(my_set) # Output: {0,1,2,3}
3.	Mutable:
Sets can be modified (elements can be added or removed)
my_set = {1,2,3}
my_set.add(4)
print(my_set) # Output: {1,2,3,4}
4.	Non-Indexable:
You cannot access set elements using an index because they are unordered.

Creating a Set:
	A set is created using curly braces {} or the set() function
	my_set = {1,2,3}
	empty_set = set() # Creates an empty set, Note: {} creates an empty dictionary
Set Operations:
1.	Add Elements
my_set = {1,2,3}
my_set.add(4)
print (my_set) # Output: {1,2,3,4}
2.	Remove Elements
Use remove() (raises an error if the element does not exist) or discard() (not error if the element does not exist)
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set) #Output: {1, 3}
3.	Set Union
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print (set1 | set2) # Output: {1,2,3,4}
4.	Set Intersection
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print (set1  & set2) # Output: {2,3}
5.	Set Difference
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print (set1 - set2) # Output: {1}
6.	Set Symmetric Difference
Elements in either set but not both
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print (set1 ^ set2) # Output: {1, 4}

Use cases/ Examples of Sets
1.	Removing Duplicates from a list:
my_list = [1,2,2,3,3]
my_set = set(my_list)
print(my_list) # Output: {1,2,3}
2.	Membership Testing:
Sets offer fast lookups using in keyword
my_set = {1,2,3}
print(2 in my_set) # Output: True
print(4 in my_set) # Output: False
3.	Mathematical Operations:
Union, intersection and difference are helpful for tasks like finding shared elements between groups, that can be helpful for venn diagrams

	Performance considerations while using sets in Python
	When using sets in Python, there are several performance considerations to keep in mind. Sets are implemented as hash tables, which makes them highly efficient for certain operations but less suitable for others.
1.	Fast Membership Testing:
Performance: Checking for membership using the in keyword is very fast in sets, with an average time complexity of O(1)
my_set = {1,2,3,4}
print(3 in my_set) # Output: True

2.	Fast Add and Remove Operations
Performance: Adding or removing elements has an average time complexity of O(1). This is because sets use a hash-based mechanism to store elements
my_set = {1,2,3}
my_set.add(4)
my_set.remove(2)
print(my_set) # Output: {1,3,4}
3.	Avoid Unhashable elements
Sets only work with hashable elements (e.g., numbers, strings, tuples). Attempting to use unhashable types like lists or other sets will raise a TypeError
Optimization Tip: Use immutable structure like tuple instead of list if you need to store similar data in a set.
4.	Duplicate Elimination is Efficient
When creating a set from an iterable (like list), duplicates are automatically removed. This is useful for duplication tasks
Performance: Converting a list to a set has an average time complexity of O(n)
my_list = [1,2,2,3,4]
my_set = set(my_list)
print (my_set) # Output: {1,2,3,4}
5.	Cost of Iteration 
Iterating over a set is slower than iterating over a list because the elements in a set are unordered and stored in hash table.
Use Case: If you need to iterate frequently and order is important, a list or tuple may be more suitable
6.	Set Operations:
Python provides several set operations like union, intersection, and difference, which are optimized
Union (|): Combines two sets; 
Intersection(&)
Difference(-)
7.	Memory Usage
Sets can be more memory-intensive than lists due to the overhead of the hash table. If memory is a constraint, consider using list or tuples if their functionality suffices
8.	Hash Collisions
The performance of sets depends on the quality of the hash function. Too much hash collisions (rare but possible) can degrade performance O(n) for operations like adding, removing and membership string.
9.	Immutable Sets (frozenset)
Use frozenset when you need an immutable set for operations like being a dictionary key or an element of another set. It provides the same performance characteristics as a regular set but ensures immutability.

"""

###############################################################################
### Set Data Type Examples
###############################################################################
print("\n####################################################################")
print ("################### Example-1 Sets are unordered ####################")
my_set = {1,2,3,5,8,7,6}

print ("my_set has elements  {1,2,3,5,8,7,6}: ", my_set)
print("##################################################################\n")


print("\n####################################################################")
print ("################### Example-2 Sets remove duplicates ####################")
my_set = {1,2,2,3,5,5,8,7,6}

print ("my_set has elements  {1,2,2,3,5,5,8,7,6}, it removes duplicate automatically: ", my_set)
print("##################################################################\n")

print("\n####################################################################")
print ("################### Example-3 Sets can be mutable ####################")
my_set = {1,2,3,5}
my_set.add(4)
print ("my_set has elements  {1,2,3,5}, it can be mutable by adding an element example value 4: ", my_set)
print("##################################################################\n")


print("\n####################################################################")
print ("################### Example-4 Sets with add operation ####################")
my_set = {1,2,3,5}
my_set.add(4)
print ("my_set has elements  {1,2,3,5}, it can be mutable by adding an element example value 4: ", my_set)
print("##################################################################\n")


print("\n####################################################################")
print ("################### Example-5 Sets with remove operation ####################")
my_set = {1,2,3,5}
my_set.remove(5)
print ("my_set has elements  {1,2,3,5}, my_set.remove(5): ", my_set)
print("##################################################################\n")

print("\n####################################################################")
print ("################### Example-6 Sets Union ####################")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print ("set1 = {1,2,3,4} and set2 = {3,4,5,6} Union of set1 and set2 (set1 | set2): ", (set1 | set2))
print("##################################################################\n")

print("\n####################################################################")
print ("################### Example-6 Sets Intersection ####################")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print ("set1 = {1,2,3,4} and set2 = {3,4,5,6} Intersection of set1 and set2 (set1 & set2): ", (set1 & set2))
print("##################################################################\n")

print("\n####################################################################")
print ("################### Example-6 Sets Difference ####################")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print ("set1 = {1,2,3,4} and set2 = {3,4,5,6} Difference of set1 and set2 (set1 - set2): ", (set1 - set2))
print("##################################################################\n")

print("\n####################################################################")
print ("################### Example-6 Sets Symmetrical Difference ####################")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print ("set1 = {1,2,3,4} and set2 = {3,4,5,6} Symmetrical Difference of set1 and set2 (set1 ^ set2): ", (set1 ^ set2))
print("##################################################################\n")


print("\n####################################################################")
print ("################### Example-6 Sets Membership Testing ####################")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print ("Checking if value 2 exists in set1 (2 in set1): ", (2 in set1))
print("##################################################################\n")


