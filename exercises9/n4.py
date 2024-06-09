#Division with Remainder Question: Write a program that takes two integers as input and
# calculates their quotient and remainder. Solution:
import math 

divisor = int(input("Number to divide by x...:"))
dividend = int(input("Number that is divided by...:"))

modulo = divisor % dividend
# One slash brings float, two bring full number 
wholeResult = divisor / dividend
print(wholeResult)
print(modulo)