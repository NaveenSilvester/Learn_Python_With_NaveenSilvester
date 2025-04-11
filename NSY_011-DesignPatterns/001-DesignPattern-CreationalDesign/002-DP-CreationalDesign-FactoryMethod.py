##################################################################################################
#### Design Pattern - Creational Design - Factory Method
##################################################################################################
"""
                Design Pattern - Creational Design - Factory Method
2.	Factory Method: Creates objects without specifying their exact class.
The Factory Method Design Pattern is creational design pattern that provides an interface for creating in a superclass but lets subclasses alter the type of objects that will be created. This allows the class to delegate the instantiation logic to its subclasses, make the code more flexible and modular
Step-by-Step Explanation of Factory Method Design Pattern
Step-1: Understand the Problem
Suppose you have a base class and several subclasses, and you need a mechanism to instantiate different subclasses based on certain conditions. Instead of explicitly calling the constructors of the subclasses, you can use the Factor Method.
Step-2: Define a Factory Class
The factory class will contain a method to handle the creation of different objects. This method will determine which class to instantiate based on the input.
Step-3: Define the Product Classes
Create a hierarchy of product classes. These are the objects to be instantiated by the factory method.
Step-4: Implement the Factory Method
The factory method is implemented in a factory class or a base class. The method decides which product class to create based on a parameter condition.

Example: Here we need to create different types of shapes (e.g., Circle, Square etc.,)
Code Implementation:
Step-1 : Define the Product Classes (Shapes)
class Shape:
	def draw(self):
		pass
class Circle(Shape):
	def draw(self):
		return (“Drawing a Circle”)

class Square(Shape):
	def draw(self):
		return (“Drawing a Square)
Step-2: Define the Factory Class
class ShapeFactory:
	def create_shape(self, shape_type):
		if shape_type == “Circle”:
			return Circle()
		elif shape_type == “Squre”:
			return Square()
		else:
			raise ValueError(f”Unknown shape type : {shape_type}”)
Step-3: Use the Factory Method to Create Objects
factory = ShapeFactory()

#Create a Circle
circle = factory.create_shape(“Circle”)
circle.draw()
square = factor.create.shape(“Square”)
square.draw()
  
Explanation of Code
1.	Product Classes (Circle and Square):
o	These are the subclasses of the Shape base class.
o	Each subclass implements the draw method specific to its type.
2.	Factory Class (ShapeFactory):
o	Contains the factory method create_shape.
o	This method takes the shape type as input and decides which subclass to instantiate.
3.	Usage:
o	The create_shape method is called with a specific shape type.
o	Based on the input, it creates and returns an object of the desired class (Circle or Square).
Benefits of Factory Method
1.	Flexibility: You can add new product classes without modifying the factory class.
2.	Reusability: The factory method centralizes object creation logic, making it reusable.
3.	Encapsulation: Subclasses decide the exact type of object to create.
"""

print ("\n####################################################################################################################")
print (""" Description:
                                        Design Pattern - Creational Design - Factory Method
Creates objects without specifying their exact class.
The Factory Method Design Pattern is creational design pattern that provides an interface for creating in a superclass but lets 
subclasses alter the type of objects that will be created. This allows the class to delegate the instantiation logic to its 
subclasses, make the code more flexible and modular
       """)
print ("####################################################################################################################\n")


print ("\n#####################################################################################################################")
print ("####################### Example Creational Design - Factory Method ###################################################")
print ("To create different types of shapes (e.g., Circle, Square etc.,)")
print ("\n#####################################################################################################################")
print ("Code Output:\n")
# Creating Base and Subclasses with common functions 
class Shape: # Base Class
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return ("Drawing a Circle")

class Square(Shape):
    def draw(self):
        return ("Drawing a Square")

# Creatig a Factory Class and then evaluate subclass based on the attribute provided and then return relevant subclass    
class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "Circle":
            return Circle()
        elif shape_type == "Square":
            return Square()
        else:
            raise ValueError (f"{shape_type} Shape not supported ")

# Creating an object of ShapeFactory 
factory = ShapeFactory()
# Invoking the subclass circle using the ShapeFactory classes evaluation method/function
circle = factory.create_shape("Circle")
square = factory.create_shape("Square")
print (circle.draw())
print (square.draw())
print ("\n#####################################################################################################################")


print ("\n#####################################################################################################################")
print ("####################### Example Creational Design - Factory Method ###################################################")
print ("To create different types of area for shapes (e.g., Circle, Square etc.,)")
print ("\n#####################################################################################################################")
print("Code Output:\n")
class Geometry:
    def __init__(self):
        pass
    def area(self):
        return ("GEm")

class Rectangle(Geometry):
    def __init__(self, Length, Width):
        super().__init__()
        self.length = Length
        self.width = Width

    def area(self):
        return (f"Area of Rectangle is: {self.length * self.width}")
    
    def perimeter(self):
        return (f"Perimeter of Rectangle is: {2 * (self.length + self.width)}")
    
    def lent(self):
        return (f"Len of Rectangle is: {self.length}")

class Circle(Geometry):
    def __init__(self, Radius):
        super().__init__()
        self.radius = Radius
    def area (self):
        return (f"Area of Circle: { 3.14 * (self.radius ** 2)}")
    def circum(self):
        return (f"Circumference of Circle: {2 * 3.14 * self.radius}")
    
class GeometryFactory:
    def create_geometry(self, shape_type, *args):
        if shape_type == "Rectangle":
            return Rectangle(*args)
        elif shape_type == "Circle":
            return Circle(*args)        
        else:
            raise ValueError ("Not Supported shape")

gf = GeometryFactory()
rectangle = gf.create_geometry("Rectangle", 10, 40)
print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.lent())
circle = gf.create_geometry("Circle", 10)
print (circle.area())
print (circle.circum())



print ("\n#####################################################################################################################")

print ("\n#####################################################################################################################")
print ("####################### Example -3 Creational Design - Factory Method ###################################################")
print ("#####################################################################################################################")
print ("Code Output:\n")
class BaseClass:
    def __init__(self):
        pass
    def area(self):
        pass

class Rectangle(BaseClass):
    def __init__(self, Length, Width):
        super().__init__()
        self.length = Length
        self.width = Width
    def area(self):
        return (f"Area of Rectangle is: {self.length * self.width}")

class Triangle(BaseClass):
    def __init__(self, Base, Height):
        super().__init__()
        self.base = Base
        self.height = Height
    
    def area(self):
        return (f"Area of Triangle is: {0.5 * self.base * self.height}")

class Circle(BaseClass):
    def __init__(self, Radius):
        super().__init__()
        self.radius = Radius
    
    def area(self):
        return (f"Area of Circle is: {3.14 * (self.radius ** 2)}")

class GeometryFactory:
    def check_geometry(self, shape_type, *args):
        if shape_type == "Rectangle":
            return Rectangle(*args)
        elif shape_type == "Triangle":
            return Triangle(*args)
        elif shape_type == "Circle":
            return Circle(*args)
        else:
            return (f"{shape_type} is not supported :-()")

mygf = GeometryFactory()
rect = mygf.check_geometry("Rectangle", 60, 40)
print (rect.area())
tri = mygf.check_geometry("Triangle", 60, 40)
print(tri.area())
circ = mygf.check_geometry("Circle", 60)
print(circ.area())
print ("#####################################################################################################################")