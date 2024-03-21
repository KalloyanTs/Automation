def factorial(n):
    i = 1
    while n > 1:
        i *= n
        n -= 1
    return i

n = (int(input(f"Provide a number:")))
print(factorial(n))