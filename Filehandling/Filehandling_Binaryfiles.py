#####################################################################################################################
### File handling - Binary Files
#####################################################################################################################
"""
Handling Binary Files
Handling binary files in Python involves working with non-text data such as images, audio files, video files, or other files stored in binary format. In Python, you can use file modes like “rb” (read binary), “wb” (write binary) or “ab” (append binary) to manage binary files.
Reading a Binary File
Example:
with open (“example.jpg”, “rb”) as file:
	binary_data = file.read()
	print (binary_data)
Writing Binary Data
Example:
binary_content = b”This is some binary data!”
with open(“binary_output.bin”, “wb”) as file:
	file.write(binary_content)
	Explanation:
•	The file is opened in "wb" mode (write binary).
•	Binary content (denoted with b) is written directly to the file.
Key Considerations When Handling Binary Files
1.	Performance:
o	For large binary files, always read/write in chunks to optimize memory usage.
2.	Binary vs. Text Mode:
o	Binary mode ("rb", "wb") processes raw data without text encoding or decoding.
o	Text mode processes text data with encoding, like UTF-8.
3.	Cross-Platform Compatibility:
o	Binary files should be handled carefully when sharing across different operating systems, as file formats may vary.

"""

print("\n#################################################################################")
print ("################### Example-1 (Filehandling - Reading Bindary file file) ########")
with open ("example.jpg", "rb") as file:
	binary_data = file.read()
	print (binary_data)
print("#################################################################################\n")

print("\n#################################################################################")
print ("################### Example-2 (Filehandling - Writing to binary file) ###########")
binary_content = b"Hello This is Binary Content\n"

with open ("BinaryFile.bin", "wb") as file:
	file.write(binary_content)
print("#################################################################################\n")