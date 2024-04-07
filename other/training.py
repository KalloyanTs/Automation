#Print Even-Indexed Characters from a String:
#Accept a string from the user and display characters that are present at an even index number.
user_string = input("Give string:")
user_list = user_string.split()

def even_index(user_list):
    return user_list[::2]

evens = even_index(user_list)
print(f"{evens}")


#Print Sum of Current and Previous Number:
#Write a program to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
#def iteration(n):
#    for n in range(10):
#        print(f"Current number {n}, previous number {n-1}, sum is {n+(n-1)}")

#n = int
#iteration(n)


#Calculate Sum and Product:
#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
#def sum_and_product(a, b):
#    c = a*b
#    if c <= 1000:
#         print(f"The product of the two numbers is: {c}")
#    else:
#         c = a+b
#         print(f"The product of the two numbers is larger than 1000, here is their sum: {c}")

#a = int(input("What is a: "))
#b = int(input("What is b: "))
#sum_and_product(a, b)



#Display Song Lyrics:
#Create a program that displays the lyrics of a song.
#file = input("File name: ")

#def read_file(file):
#    try:
#        with open(file, "r") as file_content:
#            contents = file_content.read()
#        print(contents)
#    except FileNotFoundError:
#        print("No such file")

#read_file(file)

#Print Your Name:
#Write a Python program that prints your name.

#first_name = str(input("What is your first name: "))
#last_name = str(input("What is your last name: "))

#print(f"Hello {first_name} {last_name}")
