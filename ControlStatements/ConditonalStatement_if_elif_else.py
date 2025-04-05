#####################################################################################################################
## Conditional Statement if, elif and else
#####################################################################################################################
"""
Conditional Statement
	if
		The “if” statement in Python is a control statement used to execute a block of code based on a condition. If the condition evaluates to “True”, the indented block of code under the “if” statement is executed. If the condition evaluates to “False”, the block is skipped.
	Basic Syntax of “if”
	if condition:
		# Block of code to execute if the condition is “True”
		statements(s)
	Condition: This is an expression that evaluates to “True” or “False”
Indentation: Python requires the block of code under the “if” statement to be indented.
	Example 1 : Simple if Statement
		x = 10
		if x > 5:
			print(“x is greater then 5”)
		# Output: x is greater than 5
	Example 2:  if with else
	You can use else to execute a block of code when the condition is False.
		x = 3
		if x > 5:
			print (“x is greater than 5”)
		else:
			print(“x is less than or equal to 5”)
		# Output: x is less than or equal to 5
	Example 3: if, elif and else
	You can use elif (short of “else if”) to check multiple conditions
		x = 10
		if x > 20:
			print (“x is greater than 20”)
		elif x > 10:
			print (“x is greater than 10 but less than or equal to 20”)
		else:
			prtint(“x is 10 or less”)
	# Output: x is 10 or less
	Example 4: Nested if
	You can nest if statements to check conditions within another if
		x = 15	
		if x > 10:
			if x % 2 == 0:
				print (“x is greater than 10 and even”)
			else:
				print(“x is greater than 10 and odd”)
		# Output: x is greater than 10 and odd
	Example 5: Using Logical Operators in if
	You can combine conditions using logical operators like and, or, and not
		x = 7
		if x > 5 and x <10:
			print(“x is between 5 and 10”)
		# Output: x is between 5 and 10

	Key Points to Remember
3.	Use Indentation to define the block of code under the if statement
4.	Python treats conditions like 0, None, False, or empty collections (e.g., [], {} “”) as False.
5.	You can have multiple elif blocks, but only one else block (optional)


	elif
		The elif conditional statement in Python, short for “else if”, allows you t check multiple conditions in a sequence. It provides an elegant way to handle decision-making with more than two possible outcomes. By using elif, you avoid deeply nested if statements, making your code cleaner and more readable.
Syntax
	 If condition1:
		statement(s)
	elif condition2:
		statement(s)
	else:
		statement(s)
	How it works
1.	The first if condition is evaluated.
2.	If the if condition is True, the code inside its block is executed, and the rest of the conditions are ignored.
3.	If the if condition is False, the elif condition(s) are evaluated in order.
4.	The else block is optional and executed if none of the conditions (from if or elif) are met

Example-1: Checking Multiple Conditions
	X = 20
	if x > 30:
		print (“x is greater than 3-0”)
	elif x > 20:
		print(“x is greater than 20 but less than or equal to 30”)
	elif x == 20:
		print(“x is exactly 20”)
	else:
		print(“x is 20 or less”)
	# Output: x is exactly 20
Example-2: Checking Multiple elif Conditions
You can use multiple elif conditions to handle complex decision-making.
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
# Output: Grade: B

	Example 3: Using Multiple elif blocks
	You can use multiple elif conditions to handle complex decision-making
		score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
# Output: Grade: B

Key Points to Remember
1.	Only One Block Executes: As soon as a condition is True, the corresponding block runs, and the rest are skipped.
2.	Order of Conditions Matters: Conditions are evaluated from top to bottom. If a condition is met, Python doesn’t check the ones below it.
3.	else is Optional: The else block can be omitted if not needed.
4.	Readability: Avoid placing too many elif blocks, as it can become harder to read. Consider refactoring using dictionaries or other structures for more complex logic.
	else 
The else conditional statement in Python is used as the final fallback block in an if-elif-else structure. It allows you to execute a block of code when none of the preceding if or elif conditions are met. The else block does not have a condition—it runs unconditionally when all previous conditions fail.
Syntax
if condition1:
    # Code to execute if condition1 is True
    statement(s)
elif condition2:
    # Code to execute if condition2 is True
    statement(s)
else:
    # Code to execute if none of the conditions are True
    statement(s)
	Example 1: Basic else statement
		x = 5
		if x > 10:
			print(“x is greater than 10”)
		else:
			print(“x is 10 or less”)
	# Output: x is 10 or less
	Example 2: else in and if-elif Structure
		score = 50
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
# Output: Grade: F
	Key Points to Remember
1.	Unconditional Execution: The else block is always executed if none of the preceding conditions are True.
2.	Optional: The else block is not mandatory—it can be omitted if no fallback action is needed.
3.	Placement: The else block must come after all if and elif blocks.

"""
###############################################################################
### Conditional Statement
###############################################################################
print("\n######################################################################")
print ("################### Example-1 Simple if Statement ####################")
x = 5
if x < 10:
    print ("The value of x is less than 10")
print("#######################################################################\n")

print("\n################################################################################")
print ("################### Example-2 Simple if with else Statement ####################")
x = 20
if x <= 10:
    print ("The value of x is less than 10")
else:
    print("The value of x is greater than 10")
print("################################################################################\n")

print("\n#####################################################################################")
print ("################### Example-3 Simple if, elif and else Statement ####################")
x = 10
if x > 20:
    print ("The value of x is greater than 20")
elif x > 10:
    print("The value of x is greater than 10 but less than or equal to 20")
else:
    print("The value of x is 10 or less")

print("######################################################################################\n")

print("\n#####################################################################################")
print ("################### Example-4 Nested if Statement ###################################")
x = 15
if x > 10:
    if x % 2 == 0:
        print ("The value of x is greater than 10 and is even")
    else:
        print("The value of x is greater than 10")

print("######################################################################################\n")

print("\n#####################################################################################")
print ("################### Example-5 Using logical operators################################")
x = 7
if x > 5 and x <10:
    print ("The value of x is between 5 and 10")
print("######################################################################################\n")


print("\n#####################################################################################")
print ("################### Example-6 Multiple elif conditions ################################")
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
print("######################################################################################\n")