def is_leap_year(year):
    """
    Check if a given year is a leap year.
    
    Leap year rules:
    1. If a year is divisible by 4, it's a leap year
    2. However, if it's also divisible by 100, it's NOT a leap year
    3. Unless it's also divisible by 400, then it IS a leap year
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if it's a leap year, False otherwise
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def main():
    """Main function to demonstrate the leap year checker."""
    print("Leap Year Checker")
    print("=" * 20)
    
    # Test cases
    test_years = [2000, 2020, 2024, 1900, 2100, 2023, 2025]
    
    for year in test_years:
        if is_leap_year(year):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is NOT a leap year")
    
    print("\n" + "=" * 20)
    
    # Interactive input
    try:
        user_year = int(input("Enter a year to check: "))
        if is_leap_year(user_year):
            print(f"{user_year} is a leap year!")
        else:
            print(f"{user_year} is NOT a leap year.")
    except ValueError:
        print("Please enter a valid integer year.")


if __name__ == "__main__":
    main()
