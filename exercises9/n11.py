# multiplication Table with a for Loop Question: Write a program that uses a for loop to display
# the multiplication table of a given number (up to 10). Solution

num = int(input("Enter a number: "))
for i in range(1, 11):
    product = num * i
    print(num, "x", i, "=", product)
