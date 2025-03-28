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

1 3 5 7 9
b = 9
m = 5 [b/2]
r = m
s1 = m-1
"""


b = int(input("Enter an odd digit number to be the base of the pyramid: "))

if b%2 == 0:
    print ("Please retry entering an odd number\n")
    exit()

m = b//2 + 1
print ("m is : ", m)


#b = 9
#k = b//2
#print ("K is ", k)
#m = b//2
#rows = 5

#m = 5
rows = m
#spaces = 4
spaces = m -1
reps = 1

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



        
  







'''
for ri in range(r, 0, -1):
    row = row + 1
    n = n + 1
    print ("Row number is ", row)
    if row == 1:
        for i in range(r):
            if (i == r-1):
              print ("1")
            else:
                print (" ", end="")
    else:
        row > 1
        n = n + 2
        numRep = row + 2
        print ("NumRep is : ", numRep)
        for i in range (n):
            print ("Here is ", i)
'''










"""
r = 0
for x in range(5, 0, -1):
  r = r+1
  c = x
  for i in range(c):
    if i < c-1:
     print (" ", end="")
    else:
      #print ("1")
      #print ("Line ",r)
      for n in range(r):
        if n < r-1:
          print ("1", end="")
        else:
          print ("1")

"""
   
