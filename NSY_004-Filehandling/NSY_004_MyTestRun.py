r = open("MyFile.txt", "r")
a = r.read()
r.close()
print (a)

print ("\n############################################")
print ("Readlines: reads all lines and return list")
print ("############################################")
with open ("MyFile.txt", "r") as file:
    contents = file.readlines()
    print (contents)

print ("\n############################################")
print ("readline: Reads line by line one at a time")
print ("############################################")
with open ("MyFile.txt", "r") as file:
    line = file.readline()
    line2 = file.readline()
    print (line)
    print (line2)

print ("\n############################################")
print ("Read: Reads all lines and return contents")
print ("############################################")
with open ("MyFile.txt", "r") as file:
    read_line = file.read()
    print (read_line)


print ("\n############################################")
print ("Write: Writes into file")
print ("############################################")

with open ("MyWriteFile.txt", "w") as file:
        file.write("""This is the content written by write method
               Second line written by write method
               """)


print ("\n############################################")
print ("Writelines: Writes multiple lines into file")
print ("############################################")
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("MyWriteFile.txt", "a") as file:
    file.writelines(lines)

print ("\n############################################")
print ("Seek: The seek() method moves the file pointer to a specified position")
print ("############################################")
with open("MyWriteFile.txt", "r") as file:
     file.seek(100)
     print (file.tell())
     print (file.read())
     print (file.tell())

print ("\n############################################")
print ("Tell: The tell() method returns the current position of the file pointer")
print ("############################################")
with open("MyWriteFile.txt", "r") as file:
     file.seek(100)
     print (file.tell())
     print (file.read())
     print (file.tell())

print ("\n############################################")
print ("flush: The flush() method clears the internal buffer, ensuring that all data is written to the disk")
print ("############################################")
with open("example.txt", "w") as file:
    file.write("Temporary data.")
    file.flush()


print ("\n############################################")
print ("Handling Binary Files")
print ("############################################")
with open("example.jpg", "rb") as binaryfile:
     content = binaryfile.read()
     print(content)

with open("t.jpg", "wb") as bfile:
     bfile.write(content)