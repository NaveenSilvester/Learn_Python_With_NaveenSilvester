############################################################################################################################
################################## Asynchronous Programming           ######################################################
############################################################################################################################
"""
Asynchronous Programming 
Asynchronous programming in Python is a technique that allows tasks to run concurrently without blocking the execution of other tasks. 
This is especially useful for I/O-bound tasks like file operations, network requests, or database interactions, where the program would 
otherwise be idle while waiting for a response.

Key Concepts of Asynchronous Programming in Python:
1.	Asyncio Module: The asyncio library is the heart of asynchronous programming in Python. It provides tools to write, execute, and 
manage asynchronous code using coroutines, tasks, and event loops.
2.	Coroutines: These are special functions defined with the async def keyword. They pause execution at await statements, 
allowing other tasks to run.

"""

print("\n################################################################################################################")
print("################################### Example-1 ###################################################################")
print("############################## Asynchronous Programming ##########################################################")
print("##################################################################################################################")
print("Code Output:\n")
from datetime import datetime
# Get the current time
current_time = datetime.now()

# Print the current time
print("Current Time:", current_time.strftime("%H:%M:%S"))


import asyncio
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Simulating a non-blocking delay
    print("World")
asyncio.run(say_hello())
print("##################################################################################################################")

print("\n################################################################################################################")
print("################################### Example-2 ####################################################################")
print("############################## Asynchronous Programming ##########################################################")
print("##################################################################################################################")

async def task1():
    await asyncio.sleep(2)
    print("Task 1 Complete")
    for i in range(10):
        current_time = datetime.now()
        print (f"The TASK1 {i} : {current_time.strftime("%H:%M:%S")}")


async def task2():
    await asyncio.sleep(1)
    print("Task 2 Complete")
    for i in range(10):
        current_time = datetime.now()
        print (f"The TASK2 {i} : {current_time.strftime("%H:%M:%S")}")
        

async def main():
    await asyncio.gather(task1(), task2())  # Run tasks concurrently

asyncio.run(main())
print("##################################################################################################################")