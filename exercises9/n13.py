# Sum of Even Numbers with a for Loop Question: Write a program that uses a for loop to
# calculate the sum of even numbers from 1 to 10. Solution:

sum = 0
# 2 hinten heißt: step by 2, beginne bei 2 damit Zahlen sind: (2, 4, 6, 8, 10)
for num in range(2, 11, 2): #bis 11, damit 10 noch mitgezählt wird
    sum+= num
print(sum)

2+4+6+8+10