def format_name(full_name):
    """
    Format a full name as "last,first" with proper capitalization.
    
    Args:
        full_name (str): Full name in "first last" format
        
    Returns:
        str: Formatted name as "Last,First"
    """
    # Split the name into parts and strip whitespace
    name_parts = full_name.strip().split()
    
    if len(name_parts) < 2:
        return "Error: Please enter both first and last name"
    
    # Get first and last name
    first_name = name_parts[0]
    last_name = name_parts[-1]
    
    # Capitalize first letter of each name
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    
    # Format as "last,first"
    formatted_name = f"{last_name},{first_name}"
    
    return formatted_name


def main():
    """Main function to demonstrate the name formatter."""
    print("Name Formatter - Last,First")
    print("=" * 30)
    
    # Test cases
    test_names = ["peter parker", "harry potter", "mary jane watson"]
    
    print("Examples:")
    for name in test_names:
        formatted = format_name(name)
        print(f"{name} = {formatted}")
    
    print("\n" + "=" * 30)
    
    # Interactive input
    while True:
        try:
            user_name = input("Enter full name (first last): ")
            if user_name.lower() == 'quit':
                break
                
            formatted = format_name(user_name)
            print(f"Formatted: {formatted}")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
