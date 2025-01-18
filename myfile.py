def factorial(n):
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

for num in range(6):
    print(f"The factorial of {num} is {factorial(num)}.")
