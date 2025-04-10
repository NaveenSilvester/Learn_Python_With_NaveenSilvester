##################################################################################################
#### map Function
#### map(function, *iterables)
####	The map() function in Python is a built-in tool used for applying a function to every 
####    item in an iterable, such as a list, tuple, or set. It returns a map object (an iterator) 
####    with the results. This function is particularly useful for transforming data in a concise 
####     and efficient way.
##################################################################################################
"""
map(function, iterable, ...)
IThe map() function in Python is a built-in tool used for applying a function to every item in 
an iterable, such as a list, tuple, or set. It returns a map object (an iterator) with the results.
This function is particularly useful for transforming data in a concise and efficient way.

function: A function that defines how each element in the iterable should be transformed. 
          This can be a regular function or a lambda (anonymous) function.

iterable: One or more iterables (e.g., lists, tuples). If there are multiple iterables, 
          the function is applied to corresponding elements from each.

How It Works
1. The map() function applies the function to each element of the iterable.
2. The result is a map object, which is an iterator.
3. To see the output, you can convert the map object into a list, tuple, or set.

"""

print("\n############### Example-1: Squaring Number from a list ###########################")
print('The original list contains nums = [1 ,2 , 3, 4]')
nums =[1,2,3,4]
squared = map(lambda x : x **2, nums) # Output: [1,4,9,16]
print(list(squared))
print("##################################################################################\n")


print("\n############### Example-2: Converting Strings to Uppercase ###########################")
print("The original list contains strings = ['hello', 'world']")
strings = ['hello', 'world']
upperString = map(str.upper, strings)
print(list(upperString))
print("##################################################################################\n")

