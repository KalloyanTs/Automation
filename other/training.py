# Create a matrix using for loops
def matrixes():
    rows = int(input("Rows of the matrix: "))
    columns = int(input("Columns of the matrix: "))
    matrix = []
    for n in range(rows):
        row = []
        for i in range(columns):
            number = int(input(f"Element: "))
            row.append(number)
        matrix.append(row)

    
    for row in matrix:

        print(row)
        
    reverse_matrix = matrix[::-1]
    print(reverse_matrix)  
matrixes()  

# astring = [1, 2 , 3, [33, 44 , 1 , 234]]
# for element in astring:
#     print(element)

# def training_puppy():
#     import copy
#     name = "Something"
#     new_name = copy.copy(name)
#     print(new_name.upper())
#     print(name)

# #Print Even-Indexed Characters from a String:
# #Accept a string from the user and display characters that are present at an even index number.
# def even_index(user_list: list):
#     user_string = input("Give string:")
#     user_list = user_string.split()
#     print(user_list[::2])
#     evens = even_index(user_list)
#     print(f"{evens}")

# #Print Sum of Current and Previous Number:
# #Write a program to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
# def iteration(n):
#     n = int
#     for n in range(10):
#         print(f"Current number {n}, previous number {n-1}, sum is {n+(n-1)}")

# #Calculate Sum and Product:
# #Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
# def sum_and_product(a: int, b: int):
#     c = a*b
#     a = int(input("What is a: "))
#     b = int(input("What is b: "))
#     if c <= 1000:
#          print(f"The product of the two numbers is: {c}")
#     else:
#          c = a+b
#          print(f"The product of the two numbers is larger than 1000, here is their sum: {c}")

# #Display Song Lyrics:
# #Create a program that displays the lyrics of a song.
# #file = input("File name: ")

# def read_file(file: str):
#     try:
#         with open(file, "r") as file_content:
#             contents = file_content.read()
#         print(contents)
#     except FileNotFoundError:
#         print("No such file")

# #Print Your Name:
# #Write a Python program that prints your name.

# def print_name(first_name: str, last_name: str):
#     first_name = str(input("What is your first name: "))
#     last_name = str(input("What is your last name: "))
#     print(f"Hello {first_name} {last_name}")
