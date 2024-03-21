#Program that removes divisible by 5 numbers from the list
even_numbers = [2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 , 18 , 20]
not_divbyfive = []

for num in even_numbers:
    if num % 5 != 0:
        not_divbyfive.append(num)

print(not_divbyfive)