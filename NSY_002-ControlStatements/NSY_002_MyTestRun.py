print ("---------------------------------------------------------------------------------------")
print ("IF, ELSE, ELIF Conditions")
print ("---------------------------------------------------------------------------------------")
print ("###########################################################")

var1 = "Variable One"
var2 = "Variable Two"
var3 = "Variable One"


if var1 == var2:
    print (f"var1 {var1} is identical to var2 {var2}")
else:
    print (f"var1 {var1} and var2 {var2} are not identical")

print ("###########################################################")

if var1 == var2:
    print (f"var1 ({var1}) and var2 ({var2}) are identical")
elif var1 == var3:
    print (f"var1 ({var1}) and var3 ({var3}) are identical")
elif var2 == var3:
    print (f"var2 ({var2}) and var3 ({var3}) are identical")
else:
    print ("None of them are identical")

print ("###########################################################")


print ("---------------------------------------------------------------------------------------")
print ("FOR CONTROLS")
print ("---------------------------------------------------------------------------------------")

fruits = ["apple", "orange", "fig"]
for fruit in fruits:
    print (f"{fruit}")
print ("###########################################################")

Word = "Good Morning"
for Letter in Word:
    print (f"{Letter}", end="")
print ("\n###########################################################")


students = ["Allen", "Gallen", "Kane", "Lambert"]
for index, student in enumerate(students, start=1):
    print (f"{index} : {student}")    
print ("###########################################################")


my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print (f"{key} ::: {value}")
print ("###########################################################")


print ("---------------------------------------------------------------------------------------")
print ("WHILE CONTROL")
print ("---------------------------------------------------------------------------------------")

count = 0
while (count < 5):
    print (count)
    count+=1
print ("###########################################################")


"""
response = "True"
while (response != "False"):
    response = input("Do you want to check once more (True/False)?")
    if response == "False":
        print ("Thank you!")
print ("###########################################################")

"""
count = 0

while (count<10):
    count += 1
#    print(count)
    if count == 5:

        print (" I have skipped count 5")
        continue
    else:
        print (f"{count}")
    
