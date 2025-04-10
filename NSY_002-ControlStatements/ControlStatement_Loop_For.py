#####################################################################################################################
## Control Statement For and While
#####################################################################################################################
"""
Control Statements
	for
The “for” control statement in Python is used to iterate over a sequence (such as a list, tuple, string, dictionary, or range) and execute a block of code for each element in the sequence. It is a widely used looping construct that allows you to process collections or repeat actions a specified number of times.
Basic Syntax
		for variable in sequence:
    # Code block to execute for each element in the sequence
    statement(s)
•	variable: This represents the current element in the sequence during each iteration.
•	sequence: The collection or iterable object (e.g., list, string, range, etc.) to iterate over.
Example-1 Iterating over a list
fruits = [“apple”, “orange”, “fig”]
for fruit in fruits:
	print(fruit)
	# Output: 
apple
orange 
fig
Example-2 Iterating over a String
Word = “Hello”
	for char in Word:
		print(char)
# Output:
H
e
l
l
o
		Example-3 Using Range Operator
		The range() function generates a sequence of numbers, which is often used with for loops.
for i in range(5):  # Loops from 0 to 4
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4
		Example-4 Accessing Indexes with enumerate()
		When iterating over a sequence, you can use the enumerate() function to access both the index and the element.
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
	print(f”Index is {index} : {color}”)
# Output:
 Index 0: red
 Index 1: green
 Index 2: blue

Example-5 Iterating over Dictionaries
When working with dictionaries, you can loop through keys, values, or both.
my_dict = {"a": 1, "b": 2, "c": 3}

for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# a: 1
# b: 2
# c: 3
Key Points About for Loops in Python
•	Iterables: The for loop works with any iterable, such as lists, tuples, strings, dictionaries, sets, or custom objects that implement the iterator protocol.
•	Else Clause: A for loop can optionally have an else clause, which executes if the loop completes without encountering a break.
for i in range(3):
    print(i)
else:
    print("Loop completed!")
# Output:
# 0
# 1
# 2
# Loop completed!
•	Nested Loops: You can nest for loops to iterate over multiple dimensions or sequences.

	While
	The while control statement in Python is used to create loops that execute a block of code as long as a specified condition is true. It provides flexibility when the number of iterations isn't known in advance and depends on dynamic conditions during runtime.
Basic Syntax
while condition:
    # Block of code to execute while the condition is True
    statement(s)
Condition: This is an expression that evaluates to either True or False.
The loop stops when the condition becomes False.

	Example-1: Basic while loop
	count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4
	Example-2: Using break to Exit the Loop
You can use the break statement to exit the loop prematurely.
count = 0
while True:  # Infinite loop
    print(f"Count is {count}")
    count += 1
    if count == 5:
        break  # Exit the loop when count reaches 5
# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4
	Example-3: Using continue to Skip Iterations
	The continue statement skips the rest of the code in the loop and starts the next iteration.
		count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip printing when count is 3
    print(f"Count is {count}")
# Output:
# Count is 1
# Count is 2
# Count is 4
# Count is 5
	
	Example-4: Loop with else
The else block in a while loop executes if the loop terminates normally (not through break).
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
else:
    print("Loop finished")
# Output:
# Count is 0
# Count is 1
# Count is 2
# Loop finished
	Key Points to Remember
1.	Infinite Loops: Be cautious to avoid infinite loops where the condition never becomes False
# Infinite loop example (use with care)
while True:
    print("This will run forever unless stopped!")
2.	Dynamic Conditions: Use while loops when the stopping condition depends on values that change during runtime.
3.	Performance: Ensure the condition is updated properly within the loop to prevent unnecessary iterations
4.	The while statement is versatile and especially useful for iterative tasks where the number of iterations is not predefined.

"""

###############################################################################
### Control Statements - for
###############################################################################
print("\n#################################################################################")
print ("################### Example-1 Simple for iteration over list ####################")
fruits = ["Apple", "Orange", "Fig", "Banana"]
for fruit in fruits:
    print ("Name of the fruit is : ",fruit)
print("##################################################################################\n")

print("\n#################################################################################")
print ("################### Example-2 Simple for iteration over String####################")
word = "Hello World"
for character in word:
    print (f"Charater in {word} : is {character}")
print("##################################################################################\n")

print("\n#################################################################################")
print ("################### Example-3 Using Range Operator ##############################")
for i in range(10):
    print(i)
print("##################################################################################\n")


print("\n#################################################################################")
print ("################### Example-4 Accessing Indexes with enumerate()#################")
word = "Hello World"
for index, char in enumerate(word):
    print(f"Index is {index}: Value is {char}")
print("##################################################################################\n")


print("\n#################################################################################")
print ("################### Example-5 Iterating over dictionaries #######################")
my_dict = {"a": 1, "b": 2, "c": 3}
print(f"my_dict contains \"a\": 1, \"b\": 2, \"c\": 3")
for key, value in my_dict.items():
    print(f"Key is {key}: Value is {value}")
print("##################################################################################\n")



###############################################################################
### Control Statements - while
###############################################################################

print("\n#################################################################################")
print ("################### Example-1 Basic while loop ##################################")
count = 0
while count<10:
    count += 1
    print(count)
print("##################################################################################\n")

print("\n#################################################################################")
print ("################### Example-2 Using break to Exit the Loop ######################")
count = 0
while True:
    count += 1
    print(count)
    if count == 5:
        break
print("##################################################################################\n")


print("\n#################################################################################")
print ("################### Example-3 Using continue to Skip Iterations #################")
print("Note: In the output value 3 is missing due to continue statement")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)    
print("##################################################################################\n")


print("\n#################################################################################")
print ("################### Example-3 Loop with else ####################################")
print ("""
The else block in a while loop executes if the loop terminates normally (not through break).
""")
count = 0
while count < 3:
    count += 1
    print(count) 
else:
    print("Loop Ended")   
print("##################################################################################\n")