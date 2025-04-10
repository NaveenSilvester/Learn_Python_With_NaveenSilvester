##################################################################################################
#### zip Function
#### map(function, *iterables)
#### The zip() function in Python is a built-in function that combines multiple iterables 
####  (e.g., lists, tuples, strings) into a single iterator of tuples. It works by aggregating 
####  corresponding elements from the provided iterables. The resulting zip object can be converted
####  into a list, tuple, or set for use.
##################################################################################################
"""
zip(*iterable)
The zip() function in Python is a built-in function that combines multiple iterables 
(e.g., lists, tuples, strings) into a single iterator of tuples. It works by aggregating corresponding
 elements from the provided iterables. The resulting zip object can be converted into a list, tuple, 
 or set for use.

How It Works
1. The zip() function pairs the first elements of each iterable, then the second elements, and so on.
2. If the iterables are of unequal lengths, it stops when the shortest iterable is exhausted

"""

print("\n############### Example-1: Combining two list ###########################")
print("List names = ['Alice', 'Bob', 'Charlie'] and scores = [85,90,88]\n")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]
zipped = zip(names, scores)
print(list(zipped))  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 88)]
print("##########################################################################\n")



print("\n############### Example-2: Combining two or more list ###########################")
print("List names = ['Alice', 'Bob', 'Charlie'] and scores = [85,90,88] and location = ['Bangalore', 'Mysore', 'Chennai']\n")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]
location = ["Bangalore", "Mysore", "Chennai"]
zipped = list(zip(names, scores, location))
print(zipped)  # Output: [('Alice', 85, 'Bangalore'), ('Bob', 90, 'Mysore'), ('Charlie', 88, 'Chennai')]
print("##########################################################################\n")


print("\n############### Example-3: Unzipping list ###########################")
zipped = [('Alice', 85), ('Bob', 90), ('Charlie', 88)]
names, scores = zip(*zipped)
print(type(zipped))
print(names)
print(scores)
print("##########################################################################\n")