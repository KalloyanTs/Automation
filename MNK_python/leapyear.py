yearinput = int(input("Enter year: "))
div_by_4 = yearinput % 4
div_by_100 = yearinput % 100
div_by_400 = yearinput % 400


if div_by_4 == 0 and (div_by_400 == 0 or div_by_100 != 0):
    print(f"The year {yearinput} is a leap year!")
else:
    print(f"This year {yearinput} is NOT a leap year!")