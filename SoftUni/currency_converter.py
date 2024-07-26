currency_selector = input("Specify currency to convert - USD or BGN : ")

if currency_selector == "USD":
    currency_value = float(input("Specify USD value: "))
    currency_converted = currency_value*1.79549
    print(f"{currency_value} USD is equal to {currency_converted} BGN")
elif currency_selector == "BGN":
    currency_value = float(input("Specify BGN value: "))
    currency_converted = currency_value/1.79549
    print(f"{currency_value} BGN is equal to {currency_converted} USD")
else:
    print("Invalid input currency!")