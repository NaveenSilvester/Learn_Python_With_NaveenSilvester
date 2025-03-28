"""
b = 7
r = 4
m = 4
s = 3


    1
   111
  11111
 1111111
111111111
 1111111
  11111
   111
    1

1 3 5 7 9
b = 9
m = 5 [b/2]
r = m
s1 = m-1
"""
#####################################################################################
## User inupt section
#####################################################################################

base = int(input("Enter an odd digit number to be the base of the pyramid: "))

if base%2 == 0:
    print ("Please retry entering an odd number\n")
    exit()

m = base//2 + 1
print ("m is : ", m)


#####################################################################################
## Calcuating Number of Top Pyramid Rows using User input value
## Calculating spaces of Top Pyramid 
## Calculating reps of 1 in each row for the Top pyramid
#####################################################################################

rows = m
spaces = m -1
reps = 1

#####################################################################################
## Printing Top Pyramid
#####################################################################################

for row in range(1, rows+1, 1):
   # print("#####################")
   # print ("row is ", row)
   # print ("Spaces ", spaces)
   # print ("Rep is ", reps)

    for space in range(spaces):
        print (" ", end="")
    for rep in range(reps):
        print ("1", end="")
    print ("")
    spaces = spaces - 1
    reps = reps + 2


#####################################################################################
## Calcuating Number of Bottom Pyramid Rows using User input value
## Calculating spaces of Bottom Pyramid 
## Calculating reps of 1 in each row for the Bottom pyramid
#####################################################################################

drow = rows + 1
#print ("DRW is ", drow)
nreps = base

#####################################################################################
## Printing Bottom Pyramid
#####################################################################################

for row in range(1, rows, 1):
    #print("#####################")
    #print ("row is ", drow)
    #print ("Spaces is ", row)
    drow = drow + 1
    nreps = nreps - 2
    #print ("Nreps is ", nreps)
    for nspace in range(row):
        print (" ", end="")
    for nrep in range(nreps):
        print("1", end="")
    print("")

