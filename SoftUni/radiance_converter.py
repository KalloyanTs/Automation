import math

angle_selector = input("Specify angle measurement - radiant or degree : ")
if angle_selector == "radiant":
    angle_value = float(input("Specify value in radiants: "))
    angle_converted = (angle_value*180)/math.pi
    print(f"{angle_value} radiants are equal to {angle_converted} degrees")
elif angle_selector == "degree":
    angle_value = float(input("Specify value in degrees: "))
    angle_converted = (angle_value*math.pi)/180
    print(f"{angle_value} degrees are equal to {angle_converted} radiants")
else:
    print("Invalid measurement!")