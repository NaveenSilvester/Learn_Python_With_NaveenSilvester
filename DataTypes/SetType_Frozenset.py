#####################################################################################################################
## Frozenset Data Type
#####################################################################################################################
"""
	Frozenset
	In Python, a frozenset is an immutable version of a set. Once created, its elements cannot be changed (no addition or removal). This makes it useful for scenarios where an immutable and hashable collection of unique items is needed.
Key Features of Frozenset
1.	Immutable:
Unlike a regular set, a frozenset cannot be modified after its creation. This means you cannot add or remove elements
2.	Hashable:
Since its immutable, a frozenset can be used as a key in a dictionary or as an element of another set.
3.	Unordered:
Like a set, a frozenset does not maintain any specific order of elements
4.	No Duplicates
A Frozenset automatically removes duplicate values, just like a regular set.

	Creating a Frozenset
	You can create a frozenset using the frozenset() constructor
	my_frozenset = frozenset([1,2,3,3])
	print(my_frozenset) # Output: frozenset({1,2,3})

Operations on Frozenset
	Frozensets support most set operations, but any operation that modifies a set is not allowed.
1.	Membership Testing
my_frozenset = frozenset([1,2,3])
print(2 in my_frozenset) # Output: True
2.	Union (|)
frozenset1 = frozenset([1,2,3])
frozenset2 = frozenset([3,4,5])
print(frozenset1 | frozenset2) # Output: frozenset({1,2,3,4,5})
3.	Intersection(&)
frozenset1 = frozenset([1,2,3])
frozenset2 = frozenset([3,4,5])
print(frozenset1 & frozenset2) # Output: frozenset({3})
4.	Difference(-)
frozenset1 = frozenset([1,2,3])
frozenset2 = frozenset([3,4,5])
print(frozenset1 -  frozenset2) # Output: frozenset({1,2})
5.	Symmetrical Difference(^)
frozenset1 = frozenset([1,2,3])
frozenset2 = frozenset([3,4,5])
print(frozenset1 ^ frozenset2) # Output: frozenset({1,2,4,5})

	Use Cases / Examples for Frozenset
1.	As dictionary Keys
my_dict = {frozenset([1,2,3]): “value”}
print(my_dict) # Output: {frozenset({1,2,3}): ‘value’}
2.	Membership in Sets
A frozenset can be added to a regular set because it is immutable
my_set = {frozenset([1,2]), frozen([3,4])}
print(my_set) # Output: {frozenset({1,2}), frozenset({3,4})}
3.	Data Integrity
Frozensets are great when you want to ensure that a set of data remains unchanged.
	Performance considerations while using frozenset:
	When using frozenset in Python, there are a few performance considerations to keep in mind due to its immutability and unique characteristics.
1.	Hashability:
Frozensets are hashable, meaning they can be used as keys in dictionaries or elements in other sets
Performance Benefit: Since frozensets are immutable, their hash values are fixed, making lookups in has-based data structure (like dictionaries and sets) efficient.
my_dict = {frozenset([1,2,3]) : “value”}
print(my_dict) # Output: {frozenset({1,2,3}): ‘value’}
2.	Memory Usage:
Frozensets generally have lower memory overhead comparted to mutable sets because Python does’nt need to store data for operations like additions or deletions
Consideration: While Frozensets are lightweight, larger frozenset more memory due to their content
3.	Speed of Operations:
Frozensets support set operations such as union, intersection, and difference with comparable performance of regular sets.
4.	Use in Hash-Based Structures:
Using frozensets as keys in dictionaries or elements of other sets ensures data integrity and immutability, which improves performance in scenarios requiring frequent lookups or comparisons.
5.	Immutability and Thread Safety:
Frozensets are immutable, making them inherently thread-safe. This is significant advantage in concurrent programming, where mutable objects might lead to race conditions.
Example: In multi-thread environments, frozensets can be shared across threads without worrying about unintended modifications.
6.	Initialization from Iterable
Converting an iterable to a frozenset is an O(n) operation, where n is the size of the iterable. Ensure that iterable is not unnecessarily large to avoid memory and performance bottlenecks
My_frozenset = frozenset(range(10000))
7.	Membership Testing
Like sets, frozenset allows fast membership testing using O(1) average complexity due to their has table implementation.
8.	Tradeoff with Regular Sets
Frozenset lack methods for modifying data (add, remove), making them less flexible than regular sets. Use frozensets only when immutability is essential or when the frozenset needs to be used as a dictionary key or within another set.
Use Cases
Frozensets shine in scenarios where immutability, hashability, and data integrity are priorities, such as:
o	Configuration Management: Storing fixed sets of options.
o	Data Caching: Using frozensets as unique keys for caching results.
o	Concurrency: Sharing immutable collections across threads safely.

"""

###############################################################################
### Frozenset Data Type Examples
###############################################################################
print("\n####################################################################")
print ("################### Example-1 Creating frozenset ####################")
my_frozenset = frozenset([1, 2, 2, 3])
print("Creating my_frozenset = frozenset([1,2,3,3]): ", my_frozenset)  
print("####################################################################\n")

print("\n####################################################################")
print ("################### Example-2 Membership testing ####################")
my_frozenset = frozenset([1, 2, 2, 3])
print("my_frozenset = frozenset([1,2,3,3], is 2 in my_frozenset): ", (2 in my_frozenset) ) 
print("####################################################################\n")

print("\n####################################################################")
print ("################### Example-3 Union ####################")
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
print(''' 
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
''' )
print ("Union of frozenset1 and frozenset2 (frozenset1 | frozenset2) : ", (frozenset1 | frozenset2))
print("####################################################################\n")

print("\n####################################################################")
print ("################### Example-4 Intersection ####################")
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
print(''' 
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
''' )
print ("Intersection of frozenset1 and frozenset2 (frozenset1 & frozenset2) : ", (frozenset1 & frozenset2))
print("####################################################################\n")

print("\n####################################################################")
print ("################### Example-5 Difference ####################")
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
print(''' 
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
''' )
print ("Difference of frozenset1 and frozenset2 (frozenset1 - frozenset2) : ", (frozenset1 - frozenset2))
print("####################################################################\n")

print("\n####################################################################")
print ("################### Example-6 Symmetric Difference ####################")
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
print(''' 
frozenset1 = frozenset([1, 2, 3])
frozenset2 = frozenset([3, 4, 5])
''' )
print ("Symmetric Difference of frozenset1 and frozenset2 (frozenset1 ^ frozenset2) : ", (frozenset1 ^ frozenset2))
print("####################################################################\n")