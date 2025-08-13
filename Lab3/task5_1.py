def convert_temperature():
    """
    Converts temperature between Celsius and Fahrenheit based on user's selection.
    """
    try:
        print("Temperature Converter")
        print("Select conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        choice = input("Enter 1 or 2: ").strip()
        
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        else:
            print("Invalid selection. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a numeric temperature value.")

if __name__ == "__main__":
    convert_temperature()
