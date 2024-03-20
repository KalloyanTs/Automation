# Program that asks for Name and amount and prints them all together in a sentence
first_name = str(input("What is your first name:"))
last_name = str(input("What is your last name:"))
amount = float(input("What is your balance:"))

print("Hi {} {}, you have {} in your account.".format(first_name, last_name, amount))