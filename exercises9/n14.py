# Factorial Calculation with a while Loop Question: Write a program that uses a while loop
# to calculate the factorial of a given number. Solution: n!

result = 1
n = int(input("Write the number you want a factorial of: "))

while n > 1: 
    result *= n
    n -= 1

print("The result is", result)
