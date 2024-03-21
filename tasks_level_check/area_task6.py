#Task 6: Function with Parameters and Return
#Description : Define a function calculate_area that accepts the type of shape ("circle",
#"rectangle"), and the necessary dimensions (e.g., radius for a circle, length and width for arectangle). 
#It should calculate the area and return it.



shape = str(input("Shape to calculate area:"))

def areaofshape():
    if shape == "rectangle":
        w = int(input("Rectangle width: "))
        l = int(input("Rectangle lenght: "))
        area = w * l 
        return print(f"The area of the rectangle is:{area}")
    elif shape == "circle":
        pi = 3.141592653589793238462643383279502884197
        r = int(input("Circle radius: "))
        area = pi * (r*r)
        return print(f"The area of the circle is: {area}")
    else:
        return print("Incorrect shape")

print(areaofshape())