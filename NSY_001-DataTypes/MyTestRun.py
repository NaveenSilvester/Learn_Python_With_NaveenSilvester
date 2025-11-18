print("==================================================================================\n")
print ("Numerical Datatypes")
print("==================================================================================\n")

a = -100.10

print(f"Value of a is: {a}")
print (f"Absolute value of a is :{abs(a)}")
print("#######################################################\n")
b = 10
print ("Value of b is: ", b)
print ("Value of b to the power of 3 is: ", pow(b,3))
print("#######################################################\n")

c = 21
print (f"The value of c is :{c}")
print (f"The Quotient and Reminder on dividing c by 2 is: {divmod(c,2)}")
print("#######################################################\n")

d = 10.12345678
print (f"The value of d is: {d}")
print (f"The value of d is rounded off to 6 decimals: {round(d,5)}")
print("#######################################################\n")

e = 10
print (f"The value of e is: {e}")
print (f"The Binary value of e is: {bin(e)}")
print (f"The bin() function only converts integer into Binary")
print("#######################################################\n")


f = 1000
print (f"The value of f is: {f}")
print (f"Checks if the variable is f belongs to integer class {isinstance(f, int)}")
print("#######################################################\n")

g = 5 + 3j
h = 2 + 5j
print (f"The value of g is: {g}")
print (f"The value of h is: {h}")
print (f"The value of g + h is: {g+h}")
print (f"The Real part of result is {(g+h).real}")
print (f"The Imaginary part of result is {(g+h).imag}")
print("#######################################################\n")

integer_var = 1
float_var = 2.1010
complex_var = 89 + 17j
print (f"Data type of {integer_var} is: {type(integer_var)}")
print (f"Data type of {float_var} is: {type(float_var)}")
print (f"Data type of {complex_var} is: {type(complex_var)}")
print("#######################################################\n")


print("==================================================================================\n")
print ("Sequence Datatypes")
print("==================================================================================\n")

s1 = "Hello World of Sequences"
print (f"The value of s1 is: {s1}")
print (f"The datatype of s1 is: {type(s1)}")
print("#######################################################\n")

s2 = "Allen Thomas"
print (f"The value of s2 is: {s2}")
print (f"The length of s2 is: {len(s2)}")
print (f"The value of element in 1st position of s2 is: {s2[0]}")
print (f"The value of 7th element in s2 is: {s2[6]}")
print (f"The last element of s2 is: {s2[-1]}")
print (f"The last but one element of s2 is: {s2[-2]}")
print (f"The reverse of s2 is: {s2[::-1]}")
print("#######################################################\n")

s3 = "KARNATAKA 560033"
print (f"The value of s3 is: {s3}, its length is {len(s3)}")
print (f"The value of elements between 1 to 9th position of s3 is: {s3[0:9]}")
print (f"The value of elements from 11 to 16th position is s3: {s3[10:16]}")
print (f"The value of last 6 elements of s3 is: {s3[-6:]} ")
print (f"The value of elements in s3 skipping one element is: {s3[0::2]}")
print("#######################################################\n")

s4 = "Hello World of Python"
print (f"The string s4 contains: {s4}")
print (f"The length of the string s4 is: {len(s4)}")
print (f"The datatype of s4 is: {type(s4)}")
print (f"Change the case of s4 to uppercase: {s4.upper()}")
print (f"Change the case of s4 to lower: {s4.lower()}")
print (f"Split s4 delimited by space: {s4.split(" ")}")
print("#######################################################\n")

s5 = " Sentence with Leading and Trailing spaces"
print (f"The value of s5 is: {s5}")
print (f"The value of s5 is: {s5.strip()}")
print("#######################################################\n")

s6 = "Good Morning Dear"
print (f"The value of s6 is: {s6}")
print (f"Split s6 delimited by space: {s6.split(" ")}")
s6a = s6.split(" ")
print (f"Join s6 delimited by space: {"|".join(s6.split(" "))}")
print (f"Join the split s6a into single sentence: {"|".join(s6a)}")
print (f"Replace Morning with Evening: {s6.replace("Morning","Evening")}")
print("#######################################################\n")

s7 = "Zebra has black and white stripes"
print (f"Does s7 line start with Zebra: {s7.startswith("Zebra")}")
print (f"Does s7 line ends with stripes: {s7.endswith("stripes")}")
print("#######################################################\n")

s8 = "Raj and Ram are friends. Raj is elder to Ram. Ram is married to Sita"
print (f"The value of S8 is {s8}")
print (f"The value of Ram occurs {s8.count("Ram")} times where as Raj occur only {s8.count("Raj")} times")
print("#######################################################\n")

s9 = "my.email@gmail.com"
print (f"The value of s9 is: {s9}")
print (f"Partition s9 based on @ {s9.partition  ("@")}")
print (f"Partition value of s9 from right based on . {s9.rpartition(".")}")
print("#######################################################\n")

num = "15"
print (f"value of num is: {num}")
print (f"Padding of length 6 is: {num.zfill(6)}")
print("#######################################################\n")

import re
s10 = "I from India, I am Class 12, My Phone number is 114140, my Pincode is 900870"
print (f"The valuue of s10 is: {s10}")
regpattern = r"\d+"
print (f"Fetching all numerical matches from s10: {re.findall(regpattern, s10)}")
print("#######################################################\n")

print("==================================================================================\n")
print ("List Datatypes")
print("==================================================================================\n")


l1 = ["One","Two","Three","Four","Five"]
print (f"The value of l1 is: {l1}")
print (f"The datatype of l1 is: {type(l1)}")
print (f"The number of elements in l1 is: {len(l1)}")
print (f"The First element in list l1 is: {l1[0]}")
print (f"The First letter of first element of list l1 is: {l1[0][0]}")
print (f"Concatenate elements of l1 is: {('|').join(l1)}")
l1[1] = 2
print (f"Change the second element in l1 to 2, l1: {l1}")
print("#######################################################\n")

l2 = [1,2,3,4,5]
print (f"The value of l2 is: {l2}")
l2.append(6)
print (f"Append the value 6 to l2: {l2}")
print ("Extend the list 12 by extending with [7,8,9,10]")
l2.extend([7,8,9,10])
print (f"The value of extended list l2 is: {l2}")
l2.insert(5,"Five")
print (f"Inserting Five after 5: {l2}")

print("#######################################################\n")
l3 = [11,2,3,4,5,6,7]
print(f"The value of l3 is: {l3}")
print (f"Sum of l3 is: {sum(l3)}")
print(f"Smallest value in list l3 is: {min(l3)}")
print(f"Largest value in list l3 is: {max(l3)}")

print("#######################################################\n")
l4 = [10,78,90,2,4,7,1]
print (f"The values of l4 is: {l4}")
print (f"Sorted Values of l4 in ascending order is :{sorted(l4)}")
print (f"Sorted Values of l4 in descending order :{sorted(l4, reverse=True)}")
print("#######################################################\n")

l5 = [1,4,2,3,2,4,5,1,10]
print (f"The elements in l5 list are: {l5}")
aset = set(l5)
for i in aset:
    print (f"Frequency of {i} in l5 is: {l5.count(i)}")
print("#######################################################\n")


l6 = [1,2,3,3,5,6,7]
print (f"Elements in l6 are: {l6}")
l6c = l6.copy()
print (f"Elements in l6c are: {l6c}")
l6[3] = 4
print (f"Elements in l6 are: {l6}")
print (f"Elements in l6c are: {l6c}")
print (l6)
print (l6c)

original_list = [1, 2, 3, 4, "Five"]
copied_list = original_list.copy()
original_list[4] = 99
print(original_list)  
print(copied_list)    

original_list = [1, 2, 3, 4, ["Five", "Six"],"Five"]
copied_list = original_list.copy()
original_list[4][0] = 99
print(original_list)  
print(copied_list)    
