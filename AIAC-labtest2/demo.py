"""
Demo script showing how to use the custom_sort function programmatically.
This demonstrates various test cases and usage patterns.
"""

from task1 import custom_sort, empty_list


def demo_sorting():
    """Demonstrate the custom_sort function with various test cases."""
    print("=" * 60)
    print("CUSTOM SORT FUNCTION DEMONSTRATION")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ("Empty list", []),
        ("Single element", [42]),
        ("Already sorted", [1, 2, 3, 4, 5]),
        ("Reverse sorted", [5, 4, 3, 2, 1]),
        ("With duplicates", [5, 5, 2, 2, 8, 2]),
        ("Large numbers", [1000000, 999999, 1000001, 500000]),
        ("Negative numbers", [10, -1, 0, -5, 3]),
        ("Mixed values", [-10, 0, 5, -3, 0, 1]),
        ("All negative", [-5, -1, -10, -3]),
        ("All same", [7, 7, 7, 7, 7]),
        ("Two elements", [3, 1]),
        ("Random case", [64, 34, 25, 12, 22, 11, 90])
    ]
    
    for description, test_list in test_cases:
        print(f"\n{description}:")
        print(f"  Input:  {test_list}")
        
        # Sort the list
        sorted_list = custom_sort(test_list)
        print(f"  Output: {sorted_list}")
        
        # Verify it's actually sorted
        is_sorted = all(sorted_list[i] <= sorted_list[i+1] for i in range(len(sorted_list)-1))
        print(f"  ✓ Correctly sorted: {is_sorted}")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)


def demo_empty_list():
    """Demonstrate the empty_list function with various test cases."""
    print("\n" + "=" * 60)
    print("EMPTY LIST FUNCTION DEMONSTRATION")
    print("=" * 60)
    
    # Test cases for empty_list function
    test_cases = [
        ("Empty list", []),
        ("Single element", [42]),
        ("Multiple elements", [1, 2, 3, 4, 5]),
        ("With duplicates", [5, 5, 2, 2, 8, 2]),
        ("Negative numbers", [-10, -5, -1, 0, 5]),
        ("Large numbers", [1000000, 999999, 1000001, 500000]),
        ("Mixed values", [-10, 0, 5, -3, 0, 1])
    ]
    
    for description, test_list in test_cases:
        print(f"\n{description}:")
        print(f"  Input:  {test_list} (length: {len(test_list)})")
        
        # Empty the list
        empty_result = empty_list(test_list)
        print(f"  Output: {empty_result} (length: {len(empty_result)})")
        
        # Verify it's actually empty
        is_empty = len(empty_result) == 0
        print(f"  ✓ Successfully emptied: {is_empty}")
        
        # Verify original is unchanged
        original_unchanged = test_list == test_list
        print(f"  ✓ Original unchanged: {original_unchanged}")
    
    print("\n" + "=" * 60)
    print("EMPTY LIST DEMONSTRATION COMPLETE")
    print("=" * 60)


def interactive_demo():
    """Run an interactive demo where user can test their own inputs."""
    print("\n" + "=" * 60)
    print("INTERACTIVE DEMO")
    print("=" * 60)
    print("Test the sorting function with your own inputs!")
    print("Enter 'quit' to exit the demo.")
    print()
    
    while True:
        try:
            user_input = input("Enter numbers to sort (space or comma separated): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                print("Please enter some numbers!")
                continue
            
            # Parse input
            if ',' in user_input:
                numbers = [int(x.strip()) for x in user_input.split(',') if x.strip()]
            else:
                numbers = [int(x) for x in user_input.split() if x.strip()]
            
            if not numbers:
                print("No valid numbers found!")
                continue
            
            print(f"Original: {numbers}")
            sorted_numbers = custom_sort(numbers)
            print(f"Sorted:   {sorted_numbers}")
            print()
            
        except ValueError:
            print("Invalid input! Please enter only numbers.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    # Run the sorting demonstration
    demo_sorting()
    
    # Run the empty list demonstration
    demo_empty_list()
    
    # Ask if user wants interactive demo
    print("\nWould you like to try the interactive demo? (y/n): ", end="")
    try:
        choice = input().strip().lower()
        if choice in ['y', 'yes']:
            interactive_demo()
    except KeyboardInterrupt:
        print("\nGoodbye!")
