#asks for 20 numerical values and displays the ones between 1 and 10 
numbers = [] # create empty list 

for i in range(5):
    number = int(input(f"Write your {i+1}. number here: ")) #converted to integer since input() returns a string
    # Add number to the list
    numbers.append(number)
    print(number)
print(numbers)

filtered_numbers = []
for num in numbers: 
    if 2 <= num <= 4:
        filtered_numbers.append(num)
print(filtered_numbers)