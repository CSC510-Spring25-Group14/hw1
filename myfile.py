def factorial(n):
    if n < 0 and isinstance(n, int):
        raise ValueError("Factorial is defined only for positive integers.")
        return
    if not isinstance(n, int):
        raise ValueError("Factorial is defined only for integers (positive specifically).")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

for num in range(6):
    print(f"The factorial of {num} is {factorial(num)}.")
