def AddandMultiply(x,y):
    """
    Purpose: Helps in adding and multiplying two integers
    Parameters:
        x : Integer
        y : Integer
    Return:
        Tuple containing (sum, prod)
    """
    sum = x + y
    prod = x * y
    return (sum, prod)


def square(x):
    """
    Purpose: Helps in squaring an integer
    Parameters:
        x : Integer
    Return:
        Square of a number
    """
    return (x ** 2)


def cube(x):
    """
    Purpose: Helps in cubing an integer
    Parameters:
        x : Integer
    Return:
        Cubing of a number
    """    
    return (x ** 3)


def factorial(x): 
    """
    Purpose: Helps in getting factorial of an integer
    Parameters:
        x : Integer
    Return:
        Factorial of a number
    """   
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)