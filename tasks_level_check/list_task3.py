#Task 3: List Operations
#Description : Create a list of even numbers from 1 to 20. Then, remove all numbers
#divisible by 5.
even_numbers = [2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 , 18 , 20]
not_divbyfive = []

for num in even_numbers:
    if num % 5 != 0:
        not_divbyfive.append(num)

print(not_divbyfive)