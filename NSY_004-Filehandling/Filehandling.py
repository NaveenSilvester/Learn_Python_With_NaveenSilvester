#####################################################################################################################
### File handling
#####################################################################################################################
"""
File handling
File handling in Python refers to performing operations like reading, writing, appending and closing files stored on your system. Python provides built-in functions to handle files efficiently. 
Opening a File
	Python uses the open() function to open a file. It requires a file name and mode.
File Modes:
“r”: Read mode (default)
“w”: Write Mode (Overwrites if the file exist)
“a”: Append mode (adds contents to the end of the existing file)
“b”: Binary mode (e.g., “rb”, “wb” for reading/writing binary files)
Syntax:
file = open(“file_name.txt”, “mode”) 
Example:
file = open(“example.txt”, “w”) # Opens file in write mode
file.write(“Hello World”) # Writes to file
file.close() # Closes the file 

Various File Methods
Let’s explore all the file methods used in Python file handling with detailed examples.
1. open()
The open() function is used to open a file. It requires the file name and mode.
Example:
python
file = open("example.txt", "w")  # Opens the file in write mode
file.write("Hello, World!")      # Writes to the file
file.close()                     # Closes the file
2. read()
The read() method reads the entire content of the file.
Example:
python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Prints: Hello, World!
3. readline()
The readline() method reads one line at a time.
Example:
python
with open("example.txt", "r") as file:
    first_line = file.readline()
    print(first_line)  # Prints the first line of the file
4. readlines()
The readlines() method reads all lines of the file and returns them as a list.
Example:
python
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # Prints: ['Hello, World!\n', 'Second line']
5. write()
The write() method writes a string to the file.
Example:
python
with open("example.txt", "w") as file:
    file.write("This is a new file.")
6. writelines()
The writelines() method writes multiple lines to the file. It accepts a list of strings.
Example:
python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)
7. close()
The close() method closes a file and frees system resources.
Example:
python
file = open("example.txt", "r")
file.close()
8. seek()
The seek() method moves the file pointer to a specified position.
Example:
python
with open("example.txt", "r") as file:
    file.seek(5)  # Move the pointer to the 6th character
    print(file.read())  # Reads from the new pointer position
9. tell()
The tell() method returns the current position of the file pointer.
Example:
python
with open("example.txt", "r") as file:
    file.read(10)
    print(file.tell())  # Prints: 10 (current pointer position)
10. flush()
The flush() method clears the internal buffer, ensuring that all data is written to the disk.
Example:
python
with open("example.txt", "w") as file:
    file.write("Temporary data.")
    file.flush()
11. truncate()
The truncate() method removes content from the file after the specified size.
Example:
python
with open("example.txt", "w") as file:
    file.write("Hello World!")
    file.truncate(5)  # Keeps only the first 5 characters
12. mode Attribute
The mode attribute returns the mode in which the file was opened.
Example:
python
with open("example.txt", "r") as file:
    print(file.mode)  # Output: 'r'
13. name Attribute
The name attribute returns the name of the file.
Example:
python
with open("example.txt", "r") as file:
    print(file.name)  # Output: 'example.txt'
14. closed Attribute
The closed attribute checks whether a file is closed or open.
Example:
python
file = open("example.txt", "r")
print(file.closed)  # Output: False
file.close()
print(file.closed)  # Output: True

"""

print("\n#################################################################################")
print ("################### Example-1 (Filehandling - Writing to file) ##################")
print("""
Syntax:
file = open(“file_name.txt”, "w") 

Note: File is created if not present or overwrites an already existing file
      """)
file = open("MyFile.txt", "w")
file.write("Here is my new file!\n")
file.close()
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-2 (Filehandling - Appending to file) ##################")
print("""
Syntax:
file = open(“file_name.txt”, “a”) 

Note: File is created if not present or overwrites an already existing file
      """)
file = open("MyFile.txt", "a")
file.write("Here is the second line appended to the existing file")
file.close()
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-3 (Filehandling - Reading to file) ##################")
print("""
Syntax:
file = open(“file_name.txt”, “r”) 
      """)
file = open("MyFile.txt", "r")
print(file.read())
file.close()
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-4 (Filehandling - Reading file by using with) #######")
print("""
Syntax:
    with open(“file_name.txt”, “r”) as file: 
Note: The with statement automatically handles closing the file, even in cases of errors.
      """)
with open("MyFile.txt", "r") as file:
    contents = file.read()
    print("Here are the contents in the file using 'with' keyword : \n", contents)
print("#################################################################################\n")



print("\n#################################################################################")
print ("################### Example-5 (Filehandling - Checking file existence) #######")
print("""
Use the os module to check whether a file exists
      """)
import os
if os.path.exists("MyFile.txt"):
    print ("!!!!!!!!!!!!!!!!!! File Exists !!!!!!!!!!!!!!!!!!")
    with open("MyFile.txt", "r") as file:
        contents = file.read()
        print("Here are the contents in the file using 'with' keyword : \n", contents)
else:
    print("XXXXXXX   The file does not exist in the path! XXXXXXX")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-6 (Filehandling - Deleting file) ##################")
print("""
You can also delete files using the os module.
      """)
import os

if os.path.exists("MyFile.txt"):
    os.remove("MyFile.txt")
    print("File deleted!")
else:
    print("File does not exist!")
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-7 (Filehandling - Checking file existence) #######")
print("""
Use the os module to check whether a file exists
      """)
import os
if os.path.exists("MyFile.txt"):
    print ("!!!!!!!!!!!!!!!!!! File Exists !!!!!!!!!!!!!!!!!!")
    with open("MyFile.txt", "r") as file:
        contents = file.read()
        print("Here are the contents in the file using 'with' keyword : \n", contents)
else:
    print("XXXXXXX   The file does not exist in the path! XXXXXXX")
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-8 (Filehandling - Exception handling) ###############")
print("""
Always include exception handling for robust file operations.
      """)
try:
    with open ("MyFile.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
        print("File Missing: ", e)
print("#################################################################################\n")



print("\n#################################################################################")
print ("################### Example-9 (Filehandling - Writing to file) ##################")
print("""
Syntax:
file = open(“file_name.txt”, "w") 

Note: File is created if not present or overwrites an already existing file
      """)
file = open("MyFile.txt", "w")
file.write("Here is my new file!\n Here is the Second line\n Here is the 3rd Line")
file.close()
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-10 (File method  read()) ##################")
print("""
read(): The read() method reads the entire content of the file.
      """)
try:
    with open("MyFile.txt", "r") as file:
        content = file.read()
        print("Contents of the file are: \n", content)
except FileNotFoundError as e:
    print("The File does not exist! ", e)
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-11 (File method  readline()) ##################")
print("""
readline(): The readline() method reads one line at a time.
      """)
try:
    with open("MyFile.txt", "r") as file:
        first_line = file.readline()
        print("First line of the file: \n", first_line)
except FileNotFoundError as e:
    print("The File does not exist! ", e)
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-12 (File method  readlines()) ##################")
print("""
readlines(): The readlines() method reads all lines of the file and returns them as a list.
      """)
try:
    with open("MyFile.txt", "r") as file:
        content_list = file.readlines()
        print("Conent list of lines of the file: \n", content_list)
except FileNotFoundError as e:
    print("The File does not exist! ", e)
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-13 (File method  writelines()) ##################")
print("""
writelines(): The writelines() method writes multiple lines to the file. It accepts a list of strings.
      """)
try:
    with open("MyFile.txt", "w") as file:
        my_content_list_data = ["List Data 1st Line\n", "List Data 2nd Line\n", "List Data 3rd Line\n"]
        file.writelines(my_content_list_data)
except FileNotFoundError as e:
    print("The File does not exist! ", e)
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-14 (File method  seek()) ############################")
print("""
seek(): The seek() method moves the file pointer to a specified position.
      """)
try:
    with open("MyFile.txt", "r") as file:
        file.seek(10)
        print("Reads the file after 10 characters of the file: \n", file.read())
        
except FileNotFoundError as e:
    print("The File does not exist! ", e)
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-15 (File method  tell()) ############################")
print("""
tell(): The tell() method returns the current position of the file pointer.
      """)
try:
    with open("MyFile.txt", "r") as file:
        file.seek(10)
        print("The position of the cursor : ", file.tell())
        print("Reads the file after 10 characters of the file: \n", file.read())

        
except FileNotFoundError as e:
    print("The File does not exist! ", e)
print("#################################################################################\n")


print("\n#################################################################################")
print ("################### Example-16 (File method  truncate()) ############################")
print("""
truncate(): The truncate() method removes content from the file after the specified size.
      """)
try:
    with open("MyFile.txt", "w") as file:
        file.write("Hello World!")
        file.truncate(5)       
except FileNotFoundError as e:
    print("The File does not exist! ", e)
print("#################################################################################\n")
