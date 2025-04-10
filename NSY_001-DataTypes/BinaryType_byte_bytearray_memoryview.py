#####################################################################################################################
## Binary Data Type - bytes, bytearray, memoryview
#####################################################################################################################

"""
Binary Type: 
The binary data type in Python is used to deal with binary data, which is essentially data stored in bytes. It is particularly useful when working with binary files like images, audio, or video files, as well as for tasks such as encoding or networking.
Python provides three main classes to handle binary data:
1.	bytes
This is an immutable sequence of bytes. Once created, it cannot be modified. Each byte is a number ranging from 0 to 255. This type is commonly used to handle binary data such as file, images or other data that requires direct byte-level manipulation. Once bytes object is created, its content cannot be changed.
Key Characteristics of
a.	Immutable: You cannot modify the content of a bytes object after creation.
b.	Sequence: It behaves like a sequence, so you can access individual bytes using indexing or slicing
c.	Binary Representation: Each byte is represented in its binary form, prefixed with b (e.g., b’Hello’)
Creating bytes Object
You can create a bytes object in several ways:
a.	From a Literal:
data = b’Hello’
print(data) # Output: b’Hello’
b.	From a String using Encoding:
text = “Hello”
data = bytes(text, encoding=’utf-8’)
print(data) # Output: b’Hello’
c.	From an Iterable of Integers:
numbers = [65, 66, 67]
data = bytes(numbers)
print(data) # Output: b’ABC’
d.	Empty bytes Object:
empty_data = bytes(5) # Createsa  ‘bytes’ object with 5 zeroed bytes
print(empty_data) # Output: b’\x00\x00\x00\x00\x000’
	Common Operations:
1.	Indexing and Slicing
data = b’Hello’
print(data[0]) # Output: 72 (ASCII value of ‘H’)
print(data[:2] # Output: b’He’
2.	Concatenation and Repetition
data = b’Hello’
new_data = data +  b’ World’
print(new_data) # Output: b’Hello World’ 
3.	Length
data = b’Hello’
print(len(data)) # Output: 5
4.	Writing Binary Data to File
You can use the bytes type to write binary data into a file.
data = b’This is some binary data.’
# Open the file in binary write mode and write the data 
with open (‘binary_file.bin’, ‘wb’) as file:
	file.write(data)
This creates a file named binary_file.bin and writes the binary data to it.  
5.	Reading Binary Data from a File
You can read binary data from a file using the rb mode
# Open the file in binary read mode and read the data
with open(‘binary_file.bin’, ‘rb’) as file:
	data = file.read()
print(data) # Output: b’This is some binary data.’
6.	Handling Binary Files (e.g., Image)
You can read and write image files in binary mode to copy them.
# Copy an image file
with open(‘source_image.jpg’, ‘rb’) as source:
	binary_data = source.read()
with open(‘copy_image.jpg’, ‘wb’) as copy:
	copy.write(binary_data)
7.	Appending Binary Data to File
additional_data = b’ More binary data. ‘
with open (‘binary_file.bin’, ‘ab’) as file: # ‘ab’ is append binary mode
	file.write(additional_data)
8.	Reading Specific Bytes from a File
with open(‘binary_file.bin’, ‘rb’) as file:
	file.seek(5) # Move to the 5th byte
	specific_data = file.read(10) # Read the next 10 bytes
print(specific_data)


	
	
2.	bytearray
This is mutable sequence of bytes, meaning you can modify it after creation. It is similar to the bytes data type, but unlike bytes, you can modify the content of a bytearray object after it has been created. This makes bytearray especially useful when you need to work with binary data that requires editing.

Key Characteristics of bytearray
1.	Mutable: You can modify its contents, such as replacing, inserting, or deleting bytes.
2.	Sequence: Similar to bytes, it supports indexing, slicing, and iteration.
3.	Efficient for Modifications: It’s ideal for cases where you need to manipulate byte data.
Creating bytearray Objects
You can create a bytearray object in various ways:
1.	From a Bytes Literal
data = bytearray(b’Hello’)
print(data) # Output: bytearray(b’Hello’) 
2.	From a String (with Encoding)
text = “Hello”
data = bytearray(text, encoding=’utf-8’)
print(data) # Output: bytearray(b’Hello’) 
3.	From an Iterable of Integers
numbers = [65, 66, 67]
data = bytearray(numbers)
print(data) # Output: bytearray(b’ABC’)
4.	Empty bytearray of a Specified Size
data = bytearray(5) # Creates a bytearray with 5 zeroed bytes
print(data) # bytearray(b'\x00\x00\x00\x00\x00')
Common Operations
1.	Modifying Contents
data = bytearray(b'Hello')
data[0] = 72  # ASCII value of 'H'
print(data)  # Output: bytearray(b'Hello')
2.	Appending Bytes
data = bytearray(b'Hello')
data.append(33)  # ASCII value of '!'
print(data)  # Output: bytearray(b'Hello!')
3.	Deleting Bytes
data = bytearray(b'Hello')
del data[0]
print(data)  # Output: bytearray(b'ello')
4.	Slicing and Concatenation
data = bytearray(b'Hello')
sliced = data[:3]
print(sliced)  # Output: bytearray(b'Hel')

new_data = data + bytearray(b' World')
print(new_data)  # Output: bytearray(b'Hello World')
Common Use Case 
The `bytearray` data type has several practical applications, particularly when working with binary data. Its mutability makes it ideal for situations where you need to modify data directly. Here are some common use cases:
•	Efficient Data Manipulation
The `bytearray` is often used for scenarios where you need to modify data in memory without creating new objects, which is faster and uses less memory.
Example: Editing chunks of binary data from a stream or file.
•	Networking
In network programming, `bytearray` can be used as a buffer to store incoming or outgoing binary data and modify it before transmitting or processing.
Example: Handling data packets in socket programming.
•	File Handling
When working with binary files, such as images or videos, `bytearray` is useful for reading, modifying, and writing byte-level content.
Example: Manipulating metadata within binary files.
•	Data Serialization
`bytearray` is used in serialization protocols (e.g., pickling, protobuf, etc.) to encode or decode structured binary data efficiently.
•	Text Encoding
You can use `bytearray` to work with text encoded in binary formats (e.g., UTF-8). It allows you to manipulate the text data directly at the byte level.
Example: Encoding strings or modifying parts of encoded text.



•	Custom Protocols
`bytearray` is ideal for implementing custom communication protocols that require direct manipulation of binary data, such as IoT messaging or sensor data processing.
•	Memory Buffers
In performance-critical applications, `bytearray` serves as a buffer for temporary storage and manipulation of raw binary data.
Example: Audio processing, image manipulation, or video streaming.

When to Use bytearray
•	When Binary Data Needs Modifications: Unlike bytes, you can directly change the contents of a bytearray.
•	For Performance Optimization: It’s efficient when working with large binary data that you need to alter in place, such as buffers or streams.


3.	memoryview
This provides a view of the binary data without creating a copy. It allows you to access data efficiently, especially when working with large binary files.
"""

print("\n####################################################################")
print ("################### Example-1 Create Bytes Objects ####################")
data = b'Hello'
print(data) # Output: b’Hello’

print("##################################################################\n")


print("\n###################################################################################################")
print ("################### Example-2 Create Bytes Objects From a String using Encoding ####################")
text = 'Hello'
data = bytes(text, encoding='utf-8')
print(data) # Output: b’Hello’
print("######################################################################################################\n")


print("\n###################################################################################################")
print ("################### Example-3 Create Bytes Objects From an Iterable of Integers ####################")
numbers = [65, 66, 67]
data = bytes(numbers)
print(data) # Output: b’ABC’
print("######################################################################################################\n")

print("\n###################################################################################################")
print ("################### Example-4 Create Bytes Objects Empty bytes Object ####################")
empty_data = bytes(5) # Createsa  ‘bytes’ object with 5 zeroed bytes
print(empty_data) # Output: b’\x00\x00\x00\x00\x000’

print("######################################################################################################\n")

print("\n###################################################################################################")
print ("################### Example-5  Indexing and Slicing ####################")
data = b'Hello'
print(data[0]) # Output: 72 (ASCII value of ‘H’)
print(data[:2]) # Output: b’He’
print("######################################################################################################\n")

print("\n###################################################################################################")
print ("################### Example-6 Concatenation and Repetition ####################")
data = b'Hello'
new_data = data +  b'World'
print(new_data) # Output: b’Hello World’ 
print("######################################################################################################\n")

print("\n###################################################################################################")
print ("################### Example-7 Length ####################")
data = b'Hello'
print(len(data)) # Output: 5

print("######################################################################################################\n")

print("\n###################################################################################################")
print ("################### Example-8 Writing Binary Data to File ####################")
data = b'This is some binary data.'
# Open the file in binary write mode and write the data 
with open ('binary_file.bin', 'wb') as file:
	file.write(data)
print("######################################################################################################\n")

print("\n###################################################################################################")
print ("################### Example-9 Reading Binary Data from a File ####################")
# Open the file in binary read mode and read the data
with open('binary_file.bin', 'rb') as file:
	data = file.read()
print(data) # Output: b’This is some binary data.’
print("######################################################################################################\n")

print("\n###################################################################################################")
print ("################### Example-10 Appending Binary Data to File ####################")
additional_data = b' More binary data. '
with open ('binary_file.bin', 'ab') as file: # ‘ab’ is append binary mode
	file.write(additional_data)

print("######################################################################################################\n")

print("\n###################################################################################################")
print ("################### Example-11 Reading Specific Bytes from a File ####################")
with open('binary_file.bin', 'rb') as file:
	file.seek(5) # Move to the 5th byte
	specific_data = file.read(10) # Read the next 10 bytes
print(specific_data)
print("######################################################################################################\n")

print("\n###################################################################################################")
print ("################### Example-12 Create From a Bytes Literal ####################")
data = bytearray(b'Hello')
print(data) # Output: bytearray(b’Hello’) 
print("######################################################################################################\n")