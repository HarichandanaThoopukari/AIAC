def convert_temperature():
    """
    Converts temperature between Celsius and Fahrenheit based on user input.
    """
    try:
        print("Temperature Converter")
        temp = float(input("Enter the temperature value: "))
        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C':
            converted = (temp * 9/5) + 32
            print(f"{temp}°C is {converted:.2f}°F")
        elif unit == 'F':
            converted = (temp - 32) * 5/9
            print(f"{temp}°F is {converted:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid input. Please enter a numeric temperature value.")

# Call the function if this script is run directly
if __name__ == "__main__":
    convert_temperature()
