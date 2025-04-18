##################################################################################################
#### Special Methods - Initialization and Representation
##################################################################################################
"""
Special methods in Python classes are predefined methods surrounded by double underscores (__). 
These methods allow objects to exhibit special behaviors, like built-in operations or customizing
 functionality. Here’s a list of commonly used special methods:

 Categories of Special Methods
Initialization and Representation
1.	__init__(self, ...): Constructor, initializes an object when it’s created.
2.	__repr__(self): Defines the string representation of the object (used by repr()).
3.	__str__(self): Defines the string representation used by print() and str().
	Attribute Access
1.	_getattr__(self, name): Called when accessing an attribute that doesn’t exist.
2.	__setattr__(self, name, value): Called when setting an attribute.
3.	__delattr__(self, name): Called when deleting an attribute.
	Container Methods
1.	__getitem__(self, key): Access items using square brackets (obj[key]).
2.	__setitem__(self, key, value): Set items using square brackets (obj[key] = value).
3.	__delitem__(self, key): Delete items using square brackets.
4.	__len__(self): Return the length of an object (used by len()).
5.	__iter__(self): Make an object iterable.
6.	__next__(self): Define iteration behavior.


Arithmetic Operators
1.	__add__(self, other): Implements addition (+).
2.	__sub__(self, other): Implements subtraction (-).
3.	__mul__(self, other): Implements multiplication (*).
4.	__truediv__(self, other): Implements division (/).

Comparison Operators
1.	__eq__(self, other): Implements equality (==).
2.	__ne__(self, other): Implements inequality (!=).
3.	__lt__(self, other): Implements less-than (<).
4.	__gt__(self, other): Implements greater-than (>).
5.	__le__(self, other): Implements less-than-or-equal (<=).
6.	__ge__(self, other): Implements greater-than-or-equal (>=).

Miscellaneous
1.	__call__(self, ...): Makes an object callable like a function (obj()).
2.	__del__(self): Destructor, called when an object is deleted.
3.	__contains__(self, item): Checks membership (item in obj).
4.	__hash__(self): Defines a hash value for the object (used in hash tables).
5.	__bool__(self): Returns boolean value of the object (bool(obj)).

Why Use Special Methods?
These methods allow you to:
1.	Customize built-in operations for your objects (e.g., add support for arithmetic or string representation).
2.	Make your objects behave like native types (e.g., dictionaries, lists, or functions).
3.	Create more readable and maintainable code.


"""

print ("\n####################### Example-1 (__repr__(self):)###########################################################")
print ("""
Initialization and Representation
       __repr__(self):   

       The __repr__(self) method in Python is a special method that defines the “official” string representation
of an object. It is meant to provide a precise and unambiguous description of the object, primarily for developers 
and debugging purposes. The output of repr() is often meant to be evaluable by Python's interpreter (when possible), 
or at least descriptive.     
       
Key Features of __repr__(self)
Purpose:
To return a string that would represent the object as accurately as possible.
It is used when calling repr(obj) or when inspecting the object in an interactive console.
Difference from __str__(self):
__repr__ is for developers (debugging and detailed info).
__str__ is for end-users (friendly and readable format). If __str__ is not defined, Python defaults to calling __repr__.
""")
print ("################################################################################################################\n")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_author(self):
        return (f"Author of the book is: {self.author}")

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book = Book("MyBook Title", "Allen")
print(book)
print(book.get_author())
print(book.__repr__())
print ("################################################################################################################\n")

print ("\n####################### Example-2 (__repr__(self):)###########################################################")
class Family:
    def __init__(self,father,mother,son):
        self.father = father
        self.son = son
        self.mother = mother
    
    def get_members(self):
        return (f"Father: {self.father} \n Mother: {self.mother} \n Son: {self.son}")
    
    def __repr__(self):
        return (f"Family(father='{self.father}', mother='{self.mother}' , son='{self.son}' )")

my_family = Family("Raja", "Rani", "Yuvaraja")
print (f"Repr of Family: {my_family}")
print (f"Family Members are: \n {my_family.get_members()}")
print ("################################################################################################################\n")



print ("\n####################### Example-1 (__str__(self):)###########################################################")
print ("""
__str__(self): Defines the string representation used by print() and str().
The __str__(self) method in Python is a special method used to define the string representation of an object. Its primary goal is to provide a human-readable and user-friendly description of the object. The __str__ method is called when you pass an object to str(), or when using functions like print().

Key Features of __str__(self)
1.	Human-Readable Output:
o	The focus is on presenting the object in a way that's clear and concise for the end-user.
o	This output is typically less detailed than __repr__.
2.	Default Behavior:
o	If __str__ is not defined, Python will fall back to using the __repr__ method to represent the object.
3.	Invoked When:
o	str(obj) is called.
o	The object is passed to print() or similar functions.
""")
print ("################################################################################################################\n")


class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def __str__(self):
        return (f"Name of the school {self.name} \n Location of the school {self.location}")
    
    def __repr__(self):
        return (f"School(name ='{self.name}', location = '{self.location}')  ")
    

myschool = School("SJBHS", "Bangalore")
print ("################################################################################################################\n")
print ("Since __str__ function is defined, we get to see the return of str value, else we would get return value from __repr__")
print ("\n################################################################################################################")
print("The return value from __str__ is : \n", myschool)
print ("The return value from __repr__ is : \n", myschool.__repr__())
print ("\n################################################################################################################")