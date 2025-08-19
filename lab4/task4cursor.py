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
    """Main function to get user input and count vowels."""
    print("Vowel Counter")
    print("=" * 20)
    
    # Get input from user
    user_input = input("Enter a string: ")
    
    # Count vowels
    vowel_count = count_vowels(user_input)
    
    # Display result
    print(f"Number of vowels in '{user_input}': {vowel_count}")
    
    # Show which vowels were found
    vowels_found = [char for char in user_input if char.lower() in 'aeiou']
    if vowels_found:
        print(f"Vowels found: {vowels_found}")
    else:
        print("No vowels found in the string.")


if __name__ == "__main__":
    main()
