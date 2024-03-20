import math
#Program that solves quadratic equation
def quad_equasion(a, b, c):
    d = (b*b - (4*a*c))
    if d < 0:
        print("No real roots")
    elif d == 0:
        print("x1 and x2 are equal to:", end="")
        x = (-b)/(2*a)
        return x
    elif d > 0:
         x1 = (-b + math.sqrt(d))/(2*a)
         x2 = (-b - math.sqrt(d))/(2*a)
         return x1, x2 

givea = int(input("Type the a coeficient:"))
giveb = int(input("Type the b coeficient:"))
givec = int(input("Type the c coeficient:"))

print(quad_equasion(givea, giveb, givec))