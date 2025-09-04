print("simple calculator")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


# x=input("Enter first number: ")
# y=input("Enter second number: ")
# operator=input("Enter operator (+, -, *, /): ")

# x = float(x)
# y = float(y)

# if operator == "+":
#     print("Result:", add(x, y))
# elif operator == "-":
#     print("Result:", subtract(x, y))
# elif operator == "*":
#     print("Result:", multiply(x, y))
# elif operator == "/":
#     print("Result:", divide(x, y))
# else:
#     print("Invalid operator!")
