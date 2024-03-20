def fact(i):
    if i < 0:
        print ("Can't be negative")
    else:
        if i ==0:
            return 1
        else:
            return i * fact(i-1)

number = int(input ("Type a number:"))
print("The factorial of {} is:".format(number), end=""); print(fact(number))
