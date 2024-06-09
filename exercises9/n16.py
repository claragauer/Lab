#Finding Prime Numbers with a while Loop Question: Write a program that uses a while loop
#to find prime numbers between 1 and 10. Solution:

primeNumbers = []
num = 2  # Starting from 2 because 1 is not a prime number

while num <= 10:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primeNumbers.append(num)
    num += 1

print(primeNumbers)
