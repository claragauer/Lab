# Vector Addition Question: Write a program that takes two 2D vectors (x and y components) as
# input and prints their sum. Solution:

x1 = int(input("x coordinate of first vector: "))
x2 = int(input("x coordinate of second vector: "))
y1 = int(input("y coordinate of first vector: "))
y2 = int(input("y coordinate of second vector: "))

sumX = x1 + x2
sumY = y1 + y2

print("The sum of the vectors is: ({}, {})".format(sumX, sumY))
