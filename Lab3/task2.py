def sort_list_ascending():
    """
    Function to take input list from user and sort it in ascending order
    """
    try:
        # Get input from user
        print("Enter numbers separated by spaces (e.g., 5 2 8 1 9):")
        user_input = input("Enter your list: ")
        
        # Convert input string to list of integers
        numbers = [int(x) for x in user_input.split()]
        
        # Sort the list in ascending order
        sorted_list = sorted(numbers)
        
        # Display the results
        print(f"Original list: {numbers}")
        print(f"Sorted list (ascending): {sorted_list}")
        
    except ValueError:
        print("Error: Please enter valid numbers separated by spaces")
    except Exception as e:
        print(f"An error occurred: {e}")

def sort_list_with_builtin():
    """
    Alternative method using list.sort() method
    """
    try:
        print("Enter numbers separated by spaces:")
        user_input = input("Enter your list: ")
        
        # Convert input string to list of integers
        numbers = [int(x) for x in user_input.split()]
        
        # Create a copy to avoid modifying original list
        numbers_copy = numbers.copy()
        
        # Sort the list in ascending order using sort() method
        numbers_copy.sort()
        
        print(f"Original list: {numbers}")
        print(f"Sorted list (ascending): {numbers_copy}")
        
    except ValueError:
        print("Error: Please enter valid numbers separated by spaces")

# Main execution
if __name__ == "__main__":
    print("=== List Sorting Program ===")
    print("Method 1: Using sorted() function")
    sort_list_ascending()
    
    print("\n" + "="*40 + "\n")
    
    print("Method 2: Using sort() method")
    sort_list_with_builtin()
