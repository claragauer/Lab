# Circle Circumference Calculation Question: Write a program that takes the radius of a circle as
# input and calculates its circumference. Assume the value of π as 3.14159. Solution

import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print("The circumference of the circle is:", circumference)