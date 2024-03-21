#Task 2: String Formatting
#Description : Write a Python program to accept a first name, last name, and a sum of
#money (as a float). Print a formatted string in the following form: "Hello [first_name]
#[last_name], you have $[amount] in your account."

first_name = str(input("What is your first name:"))
last_name = str(input("What is your last name:"))
amount = float(input("What is your balance:"))

print(f"Hi {first_name} {last_name}, you have {amount} in your account.")