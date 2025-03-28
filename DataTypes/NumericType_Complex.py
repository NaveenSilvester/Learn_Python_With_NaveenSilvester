
#####################################################################################################################
## Float Data Type
#####################################################################################################################
"""
Complex Numbers (complex):
•	Represents numbers with a real and imaginary part
•	Written in the form a + bj, where a is the real part and b is the imaginary part, j is the imaginary unit (SquareRoot of -1)
•	Example: 3+4j, 1-2j
C1 = 5 + 3j
C2 = -2 + 4j
Addition = C1 + C2
Subtraction = C1 - C2
Multiplication = C1 * C2
print(“Value of Addition variable is: “, Addition) # Output: (3+7j)
print(“Value of Subtraction variable is: “, Subtraction) #Output: (7-1j)
print(“Value of Multiplication variable is: “, Multiplication)  #Output: (-22+14j)


Performance Considerations while using Complex Numbers
	When working with complex numbers in Python, their performance considerations depend on the scale of operations, the size of data being processed, and the libraries being used. Here are some key points:
1.	Built-In Python Performance: Python’s built-in support for complex numbers is efficient for basic operations (addition, subtraction, multiplication etc) on small-scale datasets. However, for high-performance applications involving large datasets or repeated computations, it may not be optimal:
a.	Built-In complex number operations are performed in software rather than hardware, which may not be as fast.
b.	For small datasets, the difference is negligible, but for larger-scale computations, performance bottlenecks can occur 
2.	Using NumPy for efficiency: NumPy provides optimized support for complex numbers and is much faster than native Python for vectorized operations.
Benefits of NumPy: 
•	Vectorization: Performs operation on entire arrays without loops
•	Low-level optimizations: Uses C and hardware acceleration for efficient computation
3.	Memory Usage: Complex number in Python are stored as two float values (real and imaginary parts), which means they consume more memory compared to standard numbers. For large arrays of complex numbers, memory usage can become significant. If memory usage is critical, you can use NumPy arrays (dtype=np.complex64) to manage memory better.
4.	Alternatives for advanced use cases: For scientific and engineering applications that require extensive complex operations, specialized libraries like SciPy or performance libraries like TensorFlow might be better suited. SciPy’s signal processing module uses complex number for Fourier Transforms. TensorFlow is optimized for GPU/TPU-based computation.

"""


C1 = 5 + 3j
C2 = -2 + 4j
Addition = C1 + C2
Subtraction = C1 - C2
Multiplication = C1 * C2

print ("#######################################")
print ("Addition of Complex Numbers")
print ("#######################################")
print ("Addition of 5 + 3j and -2 + 4j: ", Addition)

#print("Value of Addition variable is: ", Addition) # Output: 
print ("\n#######################################")
print ("Subtraction of Complex Numbers")
print ("#######################################")
print ("Subtraction of 5 + 3j and -2 + 4j: ", Subtraction)

print ("\n#######################################")
print ("Multiplication of Complex Numbers")
print ("#######################################")
print ("Multiplication of 5 + 3j and -2 + 4j: ", Multiplication)


print ("\n#######################################")
print ("Accessing Real and Imaginary part of complex Numbers")
print ("#######################################")
C = 7 + 2j
print("Real Part of 7 + 2j: ", C.real) # Output: 7.0
print("Imaginary Part 7 + 2j: ", C.imag) #Output: 2.0
