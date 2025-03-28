
#####################################################################################################################
## String Data Type
#####################################################################################################################
"""
String (str):
•	Strings are arrays of Unicode characters, used for text data
•	Immutable, meaning you cannot change a string after creation
•	Example: s = “Hello World”
Key characteristics of Strings in Python
1.	Immutable
a.	Strings cannot be changed after they are created. Any modification creates a new string
Example: s = “Hello World”
	       s = s + “ Of Python” # Creates a new string
	       print (s) # Output: Hello World Of Python
	
2.	Single or Double Quotes
a.	Strings can be created using either single or double quotes

3.	Triple Quotes for multi-line strings
a.	Strings spanning multiple lines can be created using triple quotes (‘’’ or “””)
4.	Accessing Characters:
a.	Strings are indexed and support slicing. Index starts at 0
b.	Negative index starts from the end. (-1 is the last character of the string)
Example:
S = “Python”
S[0] # Output: P
S[-1] # Output: n
	Common String Methods
•	.lower() : Converts string to a lowercase. Example: “Hello”.lower() # Output: hello
•	.upper(): Converts string to uppercase. Example: “Hello”.upper() # Output : HELLO
•	.strip(): Removes leading or trailing white spaces or characters. Example: “ Hello   “.strip -> Output: Hello
•	.split(): Splits string into lists based on the delimiter (default: Space). Example: “a,b,c”.split(“,”) -> # Output: [‘a’, ’ b’,  ’ c’]
•	.join(): Joins elements of a list into a single string. Example: “,”.join([‘a’, ‘b’, ‘c’]) -> #Output: abc
•	.replace(old,new): Replaces occurrences of a substring with another substring. Example: “Python”.replace(“Py”,”Cy”) -> # Output: Cython
•	.startswith(): Checks if a string starts with a given substring. Example: “Python”.startswith(“Py”) -> # Output: True
•	.endswith(): Check if a string ends with a given substring.
Example: “Python”.endswith(“on”) - > True

	String Formatting
1.	Using f-strings (Python 3.6+):
a.	Embed variables directly into string using {}
name = “Allen”
print (f“Name is {name}”) # Output: Name is Allen

2.	Using format():
a.	Another way to insert variables into strings
print (“I love {}”.format(“Python”)) # Output: I love Python

3.	Old-style(% Operator):
a.	Still supported but less commonly used
print (“I scored %d out of %d” % (95, 100)) # Output: I scored 95 out of 100

	Escape Characters
 		Special Characters can be included using escape sequences:
•	\n : Newline
•	\t : Tab
•	\\ : Backslash
•	\’ : Single quote
•	\” : Double quote

String Slicing
	String slicing in Python is a technique used to extract a portion (or “slice”) of a string based on specific start, stop and step parameters. The Syntax for slicing is:
		String[start:stop:step]
	Here’s an explanation of each parameter:
•	start: The index where the slicing begins (inclusive). If omitted, the default is 0
•	stop: The index where the slicing ends (exclusive). If omitted, the default is the length of the string.
•	step: The interval between indices. If omitted, the default is 1
Examples:
text = “Programming”
# Basic Slicing
print(text[0:5]) # Output: Progr
print(text[3:8]) # Output: gramm
# Omitting start or stop
print(text[:6]) # Output: Progra
print(text[4:]) # Output: ramming
# Using Negative Indices
print(text[-4:]) # Output: ming
print(text[:-6]) # Output: Progr
# Using a step
print(text[0:10:2]) # Output: Pormig
print(text[::-1]) # Output: gnimmargorP


"""

print ("#######################################")
print ("Creation of String With Single Quote, Dobule Quote and triple quotes" )
print ("#######################################")
string1 = 'Hello'
string2 = "World!"
string3 = """
            This is multiline string created using triple quotes
            1. First
            2. Second
            3. Third
"""
print ("The value of string1 created by single quote: ", string1)
print ("The value of string2 created by double quote: ", string2)
print ("The value of string3 is: ", string3)

print ("\n#######################################")
print ("Formatting Strings - (f-string)" )
print ("Introduced in Python 3.6, f-strings make string formatting more concise:")
print ("#######################################")
name = "Allen"
age = 14
print (f"{name} is {age} years old")

print ("\n#######################################")
print ("Formatting Strings - (raw-string)" )
print ("Raw strings are prefixed with r and are useful for paths or regular expressions")
print ("#######################################")
path = r"C:\User\Name"
print (path)

print ("\n#######################################")
print ("Formatting Strings - format()" )
print ("Another way to insert variables into strings")
print ("#######################################")
print ("I love {}".format("Python Programming"))

print ("\n#######################################")
print ("Formatting Strings - % operator" )
print ("Another way to insert variables into strings")
print ("#######################################")
print ("I scored %d out of %d" % (95, 100))

print ("\n#######################################")
print ("Indexing Strings" )
print ("Positive Indexing")
print ("#######################################")
text = "Allen"
print("The value at index 0 of Allen is: ", text[0])
print("The value at index 3 of Allen is: ", text[3])


print ("\n#######################################")
print ("Indexing Strings" )
print ("Negative Indexing")
print ("#######################################")
text = "Allen"
print("The value at index -1 of Allen is: ", text[-1])
print("The value at index -3 of Allen is: ", text[-3])

print ("\n#######################################")
print ("Slicing Strings" )
print ("""
. The Syntax for slicing is:
		String[start:stop:step]
	Here’s an explanation of each parameter:
•	start: The index where the slicing begins (inclusive). If omitted, the default is 0
•	stop: The index where the slicing ends (exclusive). If omitted, the default is the length of the string.
•	step: The interval between indices. If omitted, the default is 1
""")
print ("Basic Slicing")
print ("#######################################")
text = "Programming"
print ("Print First 5 elements of a text Programming: ", text[0:5])
print ("Print Elements from 3 to 5 of a text Programming: ", text[2:5])


print ("\n#######################################")
print ("Slicing Strings" )
print ("""
. The Syntax for slicing is:
		String[start:stop:step]
	Here’s an explanation of each parameter:
•	start: The index where the slicing begins (inclusive). If omitted, the default is 0
•	stop: The index where the slicing ends (exclusive). If omitted, the default is the length of the string.
•	step: The interval between indices. If omitted, the default is 1
""")
print ("Omitting Start or Stop")
print ("#######################################")
print ("Print First 5 elements of a text Programming: ", text[:5])
print ("Print Elements from 3 to end of a text Programming: ", text[2:])


print ("\n#######################################")
print ("Slicing Strings" )
print ("""
. The Syntax for slicing is:
		String[start:stop:step]
	Here’s an explanation of each parameter:
•	start: The index where the slicing begins (inclusive). If omitted, the default is 0
•	stop: The index where the slicing ends (exclusive). If omitted, the default is the length of the string.
•	step: The interval between indices. If omitted, the default is 1
""")
print ("Using Negative Indices")
print ("#######################################")
print ("Print all elements of a text Programming except the begining from 6th character from the last: ", text[-6:])
print ("Print Elements from start to last but two elements of a text Programming: ", text[:-2])


print ("\n#######################################")
print ("Slicing Strings" )
print ("""
. The Syntax for slicing is:
		String[start:stop:step]
	Here’s an explanation of each parameter:
•	start: The index where the slicing begins (inclusive). If omitted, the default is 0
•	stop: The index where the slicing ends (exclusive). If omitted, the default is the length of the string.
•	step: The interval between indices. If omitted, the default is 1
""")
print ("Using Step")
print ("#######################################")
print ("Print all alternate elements of a text Programming upto 10th character begining from first character : ", text[:10:2])
print ("Print Elements from start to last in reverse for a text Programming: ", text[::-1])

print ("\n#######################################")
print ("Extracting File Name and extensions" )
file = "Example.txt"
print("File name: ", file[:-4])
print("File extension: ", file[-3:])

print ("\n#######################################")
print ("Extracting file name from a file path" )
path = "/user/docs/report.pdf"
file_name = path.split('/')[-1]
print(file_name)  # Output: report.pdf


print ("\n#######################################")
print ("Changing Case" )
text = "Hello Naveen Silvester"
print("Changing every letter in the string to lower case: ", text.lower())
print("Changing every letter in the string to upper case: ", text.upper())
print("Changing only First letter in the string to Capital case: ", text.capitalize())
print("Swapping case of every letter in the string: ", text.swapcase())



print ("\n#######################################")
print ("Checking string properties" )
text = "Programming123"
print("Check if all characters are alphabets in Programming123: ", text.isalpha())
print("Check if all characters are digits in Programming123: ", text.isdigit())
print("Check if all characters are alphanumeral in Programming123: ", text.isalnum())
print("Check if Programming123 begins with Pro: ", text.startswith("Pr"))
print("Check if Programming123 ends with 123: ", text.endswith("123"))

print ("\n#######################################")
print ("Modifying Strings" )
text = " I love India   "
print("Removing white spaces at the begining and ending of the string")
print ("The clean string is: ", text.strip())
print("Replacing India with Indians: ", text.replace("India", "Indian"))
print ("Spliting the string with space delimiter into an array: ", text.split())


print ("\n#######################################")
print ("Joining Strings" )
text = ["I", "Love", "Python", "Programming"]
print ("Joining the list into a string by a space delimiter: ", " ".join(text))

print ("\n#######################################")
print ("Substring Strings" )
text = "I love Python programming, because Python Programming is facinating"
print ("Count the number of time Python is repeated in the string: ", text.count("Python"))
print ("Find the index of the term time Python in the string (First occurence): ", text.find("Python"))
print ("Check if the term Programming exists in the text: ", "Programming" in text)
print ("Check if the term Java not exists in the text: ", "Java" not in text)