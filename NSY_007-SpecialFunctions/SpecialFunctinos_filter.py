##################################################################################################
#### Filter Function
#### filter(function, iterable)
####	Filters elements of an iterable based on condition.
##################################################################################################
"""
filter(function, iterable)
In Python, the filter() function is used to filter elements from an iterable (e.g., list, tuple, set) 
based on a condition. It applies a function (usually a lambda function or a predefined one) to each 
item in the iterable and returns an iterator containing only the elements that satisfy the condition.
function: A function that returns True or False. If None is passed, it filters out elements that are 
          considered False (e.g., 0, None, False, empty strings).
iterable: The collection of items you want to filter.


How It Works
The filter() function goes through each element in the iterable:
Passes the element to the function.
Includes the element in the output if the function evaluates to True.
The result is a filter object, which is an iterator. You can convert this object to a list, tuple, etc., 
or iterate through it.
"""

print("\n############### Example-1: Filter out evens from the list ###########################")
print('The original list contains nums = [1 ,2 , 3, 4]')
nums = [1 ,2 , 3, 4]
evens = filter(lambda x : x %2 == 0, nums) #Output: [2,4]  
print (list(evens))
print("######################################################################################\n")



print("\n############### Example-2: Filter out blanks from the list ###########################")
print('Original list string = ["apple", "", "banana", "cherry", ""] ')
strings = ["apple", "", "banana", "cherry", ""]
non_empty = filter(None, strings)
print(list(non_empty))  # Output: ['apple', 'banana', 'cherry']
print("######################################################################################\n")