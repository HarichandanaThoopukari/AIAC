def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def main():
    
    try:
        # Get input from user
        user_input = input("Enter a number to calculate factorial: ")
        
        # Convert to integer
        number = int(user_input)
        
        # Calculate factorial
        result = factorial(number)
        
        # Print the result
        if isinstance(result, str):
            print(result)
        else:
            print(f"Factorial of {number} is: {result}")
            
    except ValueError:
        print("Error: Please enter a valid integer")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()











