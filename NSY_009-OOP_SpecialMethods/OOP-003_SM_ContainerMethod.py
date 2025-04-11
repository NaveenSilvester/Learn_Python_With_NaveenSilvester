##################################################################################################
#### Special Methods - Container Method
##################################################################################################
"""
1.	__getitem__(self, key): Access items using square brackets (obj[key]).
The __getitem__(self, key) method in Python is used to retrieve an item from an object using the subscript notation (e.g., obj[key]). It is a special or magic method that enables custom behavior for indexing objects. You can define this method in your class to make objects of that class behave like dictionaries, lists, or other built-in sequence types.

class MyList:
	def __init__(self, items):
		self.items = items
	
	def __getitem__(self, index):
		return self.items[index]

# Create an instance of the MyList class
my_list = My_List([10, 20, 30, 40])

# Access items using subscript notation
print(my_list[0]) # Output: 10
print(my_list[2]) # Output: 30

In this example:
1.	The MyList class takes a list as input and stores it in the self.items attributes
2.	The __getitem__ method is implemented to return an item from self.items based on the index provided
3.	Using subscript notation (my_list[0] or my_list[2]) calls the __getitem__ method internally
This method is particularly useful for custom container objects when you want to enable flexible indexing or slicing.

"""
print ("####################################################################################################################\n")

print ("\n####################### Example-1 (__getitem__(self items):)###########################################################")
class MyList:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]

my_list = MyList([10,20,30,40,50])
print (my_list[0])
print (my_list[4])
print ("####################################################################################################################\n")

print ("\n####################### Example-2 (__getitem__(self items):)###########################################################")

class URLMapping:
    def __init__(self):
        self.urls = {"home" : "example.com/home", "about" : "example.com/about"}
    
    def __getitem__(self, key):
        return self.urls.get(key, "404 Not Found")

urls = URLMapping()
print (urls["home"])
print ("####################################################################################################################\n")

print ("\n####################### Example-3 (Simple Function)###########################################################")
print ("####################################################################################################################\n")
def myurl(item):
    urls = {"home" : "example.com/home", "about" : "example.com/about"}
    try:
        if urls[item] != "":
            return (urls[item])
    except:
        return (f"{item} Page Not Found")

print (f"myurl is {myurl('home')}")
print (f"{myurl('Location')}")
print ("####################################################################################################################\n")


