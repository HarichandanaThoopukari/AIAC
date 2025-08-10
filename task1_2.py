def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

number = 5  # You can change this number to calculate factorial of another number
print(f"Factorial of {number} is: {factorial(number)}")
