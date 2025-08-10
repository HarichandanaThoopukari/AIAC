def factorial(n):
    """
    Calculate the factorial of a given number.
    """
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Programmer provides the input number here
number = 5  # Change this number to calculate factorial of different numbers

# Calculate and display the factorial
result = factorial(number)
print(f"Factorial of {number} is: {result}")
