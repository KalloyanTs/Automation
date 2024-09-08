square_meters = float(input())
final_price = 7.61*square_meters
discount = final_price*0.18
discounted_price = final_price - discount
if 0 <= square_meters <= 10000:
    print(f"The final price is: {discounted_price} lv.")
    print(f"The discount is: {discount} lv.")
else:
    raise SystemError