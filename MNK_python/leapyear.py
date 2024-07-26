yearinput = int(input("Enter year: "))
if yearinput % 4 == 0 and (yearinput % 400 == 0 or yearinput % 100 != 0):
    print(f"The year {yearinput} is a leap year!")
else:
    print(f"This year {yearinput} is NOT a leap year!")