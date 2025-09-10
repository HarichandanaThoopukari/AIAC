def safe_divide(a, b):
    """Safely divides a by b, raising an error if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b



if __name__ == "__main__":
    while True:
        try:
            a = float(input("Enter value for a: "))
            b = float(input("Enter value for b: "))
            result = safe_divide(a, b)
            print(f"Result of {a} / {b} is {result}")
            break
        except ValueError as error:
            print("Error:", error)
            print("Please try again.")
    print("End of program")