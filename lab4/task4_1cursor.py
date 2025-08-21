def count_vowels(text):
    """
    Count the number of vowels in a given string.
    
    Args:
        text (str): Input string to count vowels in
        
    Returns:
        int: Number of vowels in the string
    """
    vowels = 'aeiouAEIOU'
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count


def main():
    """Main function to demonstrate vowel counting with example and user input."""
    print("Vowel Counter")
    print("=" * 30)
    
    # Show the example
    example = "sruniversity"
    example_count = count_vowels(example)
    print(f"Example: {example}")
    print(f"Vowel count = {example_count}")
    # Show the vowels found in the example
    vowels_found = [char for char in example if char.lower() in 'aeiou']
    print(f"Vowels found: {vowels_found}")
    print("\n" + "=" * 30)
    # Get input from user
    user_input = input("Enter a string: ")
    # Count vowels in user input
    user_count = count_vowels(user_input)
    # Display result
    print(f"Vowel count = {user_count}")
    # Show which vowels were found
    user_vowels = [char for char in user_input if char.lower() in 'aeiou']
    if user_vowels:
        print(f"Vowels found: {user_vowels}")
    else:
        print("No vowels found in the string.")
if __name__ == "__main__":
    main()
