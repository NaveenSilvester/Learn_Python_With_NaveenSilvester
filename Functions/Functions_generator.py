#####################################################################################################################
### Functions - Generator Functions in Python
#####################################################################################################################

"""
Generator Functions
	These are functions that return an iterator object and use “yield” instead of “return”. They are memory efficient for iterating over large datasets. When a function contains “yield”, it becomes a generator.
Step-by-Step Explanation
1.	Defining a Generator Function
•	A generator function looks like a normal function but contains one or more “yield” statements.
def my_generator():
	yield 1
	yield 2
	yield 3 
2.	Using Generator
•	To use the generator, you need to call the function. It returns a generator object rather than executing the function.
gen = my_generator() # Creates a generator object
print(next(gen)) # Outputs: 1
print(next(gen)) # Outputs: 2
print(next(gen)) # Outputs: 3 
3.	Yield Instead of Return
•	The yield keyword pauses the function, saving its state for the next iteration. When next() is called again, the generator resumes from where it left off.
4.	Iterating Through a Generator
•	Generators can be looped through using a “for” loop, which automatically handles calling next()
for value in my_generator():
	print(value)

Why are Generators Memory Efficient?
•	On-the-fly computation: Generators produce items one at a time only when needed. This means they don’t store the entire sequence in memory.
•	No Data Duplication: Instead of loading a large dataset into memory, generators compute each time as required.
def infinite_sequence():
	n = 0
	while True:
		yield n
		n += 1
•	Comparison with lists: Let’s consider generating a list of numbers
# List
numbers = [x for x in range(1000000)] # Takes up a lot of memory
		# Generator
		numbers = ( x for x in range(1000000)) # Uses generator expression
•	The list comprehension allocated memory for all 1000000 items upfront.
•	The generator expression computes each value only when required, saving memory
Visualizing the Memory Efficiency
	Here’s an example to illustrate memory usage:
	import sys
	# List
	num_list = [x for x in range(1000000)]
	print(“Memory used by list: “, sys.getsizeof(num_list), “bytes”)
	
	# Generator
	num_gen = (x for x in range(1000000))
	print(“Memory used by generator:”, sys.getsizeof(num_gen), “bytes”)
	
Output:
	A list may take tens or hundreds of times more memory compared to a generator.
Generators are excellent for scenarios like:
•	Handling large datasets (E.g., reading files line by line)
•	Infinite sequences
•	Streaming real-time data.

"""

print("\n#################################################################################")
print ("################### Example-1 (Comparison of normal list with Generator) ########")
print("Creating a num_list of 1000000 using list comprehension and printing it")
num_list = [x for x in range(100)]
print(num_list)
print("Creating a gen_list of 1000000 using Generator and printing it")
gen_list = (x for x in range(100))
print(type(gen_list))
for value in gen_list:
    print(value)
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-2 (Comparison of Memory utilizaton Generator) #######")
print("Creating a num_list of 1000000 using list comprehension and printing it")
import sys
num_list = [x for x in range(1000000)]
print("Memory used by the num_list of 1000000 is : ", sys.getsizeof(num_list), " bytes")

print("Creating a gen_list of 1000000 using Generator and printing it")
gen_list = (x for x in range(1000000))
print("Memory used by the gen_list of 1000000 is : ", sys.getsizeof(gen_list), " bytes")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-3 (Comparison of Time efficieny Generator) #######")
print ("""
    List Comprehension:
        Time Efficiency:
            Faster for small datasets, as the entire list is created in memory upfront.
            All values are computed and stored immediately, making subsequent access very fast.

    Generator:
        Time Efficieny:
            More time-efficient for large datasets or when you don’t need to access all items.
            Values are computed lazily (on the fly), which might take slightly longer per individual item but saves memory.
    
    In general:
        List comprehensions might be faster when you need to repeatedly access or modify the entire dataset.
        Generators are better for streaming or when you don’t need all items at once.
       Which one to use depends on your use case. Memory efficiency or lazy evaluation? Generators win. 
       Speed with small, manageable data? List comprehensions excel. 😊
       """)
import timeit

# Code to be measured for list comprehension
code_to_listComprehension = """
num_list = [x for x in range(10)]
print(num_list)
"""

# Code to be measured for generator
code_to_generator = """
gen_list = (x for x in range(10))
for value in gen_list:
    print(value)
"""

# Measure execution time
execution_time_listComprehension = timeit.timeit(code_to_listComprehension, number=1)
execution_time_generator = timeit.timeit(code_to_generator, number=1)

print(f"Average time taken over 1 runs for list comprehension: {execution_time_listComprehension} seconds")
print(f"Average time taken over 1 run for generator: {execution_time_generator} seconds")
print("#################################################################################\n")

