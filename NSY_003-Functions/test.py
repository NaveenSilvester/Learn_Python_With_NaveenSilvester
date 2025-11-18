numbers = [5, 12, 17, 18, 24, 32]
print(list(filter(lambda x : x%2 == 0, numbers)))


fruits = ["apple", "banana", "avocado", "cherry", "apricot"]
def getbyletter(c, list):
    mylist = []
    for item in list:
        if item.startswith(c):
            mylist.append(item)
    return mylist

g = getbyletter("a",fruits)
print (g)

a = [ item for item in fruits if item.startswith("a")]
print (f"HERE is the list {a}")

al = list(filter(lambda item : item.startswith("a"), fruits ))
print (f"List is {al}")