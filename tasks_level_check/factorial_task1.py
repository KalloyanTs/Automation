#Task 1: Number Manipulation
#Description : Write a Python program to calculate the factorial of a given number.

def fact(i):
    if i < 0: #We cannot give a factorial from a negative number, need to exclude it
        print ("Can't be negative")
    else: #Need to factor that 0 is an exception.
        if i ==0:
            return 1
        else:
            return i * fact(i-1) #this will make it so that every number will be multiplied by itself -1 and then go through the function again until it reaches 0, then it will return 1

number = int(input ("Type a number:")) # Ask for a input number
print(f"The factorial of {number} is:", end=""); print(fact(number)) #Print the resulting number
