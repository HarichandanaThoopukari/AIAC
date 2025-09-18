def custom_sort(arr):
    """
    Sort an array using bubble sort algorithm.
    
    Args:
        arr (list): List of numbers to be sorted
        
    Returns:
        list: Sorted list in ascending order
    """
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    
    # Bubble sort implementation
    for i in range(len(sorted_arr)):
        for j in range(i+1, len(sorted_arr)):
            if sorted_arr[i] > sorted_arr[j]:
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]
    return sorted_arr


def empty_list(arr):
    """
    Empty a list by removing all elements.
    
    Args:
        arr (list): List to be emptied
        
    Returns:
        list: Empty list
    """
    # Create a copy to avoid modifying the original list
    empty_arr = arr.copy()
    empty_arr.clear()
    return empty_arr


def get_user_input():
    """
    Get input from user and convert to list of numbers.
    
    Returns:
        list: List of numbers entered by user
    """
    print("Enter numbers to sort (separated by spaces or commas):")
    print("Examples: '5 3 1 4 2' or '5,3,1,4,2' or '5, 3, 1, 4, 2'")
    
    while True:
        try:
            user_input = input("Your input: ").strip()
            
            if not user_input:
                print("Please enter some numbers!")
                continue
            
            # Handle both space and comma separated inputs
            if ',' in user_input:
                # Split by comma and clean whitespace
                numbers = [x.strip() for x in user_input.split(',')]
            else:
                # Split by spaces
                numbers = user_input.split()
            
            # Convert to integers
            number_list = []
            for num_str in numbers:
                if num_str:  # Skip empty strings
                    number_list.append(int(num_str))
            
            if not number_list:
                print("No valid numbers found. Please try again!")
                continue
                
            return number_list
            
        except ValueError:
            print("Invalid input! Please enter only numbers separated by spaces or commas.")
        except KeyboardInterrupt:
            print("\nExiting...")
            return None


def main():
    """Main function to run the sorting program with user input."""
    print("=" * 50)
    print("CUSTOM SORTING PROGRAM")
    print("=" * 50)
    print("This program sorts a list of numbers using bubble sort algorithm.")
    print("Available operations: sort, empty list")
    print()
    
    while True:
        # Get input from user
        numbers = get_user_input()
        
        if numbers is None:  # User pressed Ctrl+C
            break
            
        print(f"\nOriginal list: {numbers}")
        print(f"List length:   {len(numbers)}")
        
        # Ask what operation to perform
        print("\nWhat would you like to do?")
        print("1. Sort the list")
        print("2. Empty the list")
        print("3. Both (sort then empty)")
        
        while True:
            try:
                choice = input("Enter your choice (1/2/3): ").strip()
                
                if choice == '1':
                    # Sort the numbers
                    sorted_numbers = custom_sort(numbers)
                    print(f"Sorted list:   {sorted_numbers}")
                    break
                    
                elif choice == '2':
                    # Empty the list
                    empty_numbers = empty_list(numbers)
                    print(f"Emptied list:  {empty_numbers}")
                    print(f"New length:    {len(empty_numbers)}")
                    break
                    
                elif choice == '3':
                    # Both operations
                    sorted_numbers = custom_sort(numbers)
                    print(f"Sorted list:   {sorted_numbers}")
                    
                    empty_numbers = empty_list(sorted_numbers)
                    print(f"Emptied list:  {empty_numbers}")
                    print(f"Final length:  {len(empty_numbers)}")
                    break
                    
                else:
                    print("Invalid choice! Please enter 1, 2, or 3.")
                    
            except KeyboardInterrupt:
                print("\nExiting...")
                return
        
        # Ask if user wants to continue
        print("\n" + "-" * 30)
        while True:
            continue_choice = input("Perform another operation? (y/n): ").strip().lower()
            if continue_choice in ['y', 'yes']:
                print()
                break
            elif continue_choice in ['n', 'no']:
                print("Thank you for using the sorting program!")
                return
            else:
                print("Please enter 'y' or 'n'")


if __name__ == "__main__":
    main()
