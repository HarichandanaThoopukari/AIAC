def cm_to_inches(cm):
    """
    Convert centimeters to inches.
    Args:
        cm (float): Length in centimeters     
    Returns:
        float: Length in inches  
        """
    # 1 inch = 2.54 centimeters
    inches = cm / 2.54
    return inches
def main():
    """Main function to demonstrate the centimeter to inch converter."""
    print("Centimeter to Inch Converter")
    print("=" * 30)
    # Test case
    test_cm = 10.0
    test_inches = cm_to_inches(test_cm)
    print(f"Example: {test_cm} centimeters is equal to {test_inches:.6f} inches.")
    print("\n" + "=" * 30)  
    # Interactive input
    try:
        user_cm = float(input("Enter length in centimeters: "))
        user_inches = cm_to_inches(user_cm)
        print(f"{user_cm} centimeters is equal to {user_inches:.6f} inches.")
    except ValueError:
        print("Please enter a valid number.")
if __name__ == "__main__":
    main()
