def calculate_power_bill():
    """
    Function to calculate power bill based on previous and present units
    """
    try:
        # Get input from user
        print("=== Power Bill Calculator ===")
        
        # Get previous units
        previous_units = float(input("Enter previous month units: "))
        
        # Get present units
        present_units = float(input("Enter present month units: "))
        
        # Calculate units consumed
        units_consumed = present_units - previous_units
        
        # Calculate bill based on units consumed
        if units_consumed <= 0:
            print("Error: Present units should be greater than previous units")
            return
        
        # Define rate structure (example rates - can be modified)
        if units_consumed <= 100:
            rate_per_unit = 2.50
        elif units_consumed <= 200:
            rate_per_unit = 3.50
        elif units_consumed <= 300:
            rate_per_unit = 4.50
        else:
            rate_per_unit = 5.50
        
        # Calculate total bill
        total_bill = units_consumed * rate_per_unit
        
        # Display the results
        print("\n=== Bill Details ===")
        print(f"Previous month units: {previous_units}")
        print(f"Present month units: {present_units}")
        print(f"Units consumed: {units_consumed}")
        print(f"Rate per unit: ${rate_per_unit}")
        print(f"Total bill: ${total_bill:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"An error occurred: {e}")

def calculate_power_bill_with_tax():
    """
    Function to calculate power bill with tax included
    """
    try:
        print("\n=== Power Bill Calculator with Tax ===")
        
        # Get input from user
        previous_units = float(input("Enter previous month units: "))
        present_units = float(input("Enter present month units: "))
        
        # Calculate units consumed
        units_consumed = present_units - previous_units
        
        if units_consumed <= 0:
            print("Error: Present units should be greater than previous units")
            return
        
        # Calculate base bill
        if units_consumed <= 100:
            rate_per_unit = 2.50
        elif units_consumed <= 200:
            rate_per_unit = 3.50
        elif units_consumed <= 300:
            rate_per_unit = 4.50
        else:
            rate_per_unit = 5.50
        
        base_bill = units_consumed * rate_per_unit
        
        # Calculate tax (example: 10% tax)
        tax_rate = 0.10
        tax_amount = base_bill * tax_rate
        
        # Calculate total bill with tax
        total_bill = base_bill + tax_amount
        
        # Display detailed results
        print("\n=== Detailed Bill ===")
        print(f"Previous month units: {previous_units}")
        print(f"Present month units: {present_units}")
        print(f"Units consumed: {units_consumed}")
        print(f"Rate per unit: ${rate_per_unit}")
        print(f"Base bill: ${base_bill:.2f}")
        print(f"Tax ({tax_rate*100}%): ${tax_amount:.2f}")
        print(f"Total bill: ${total_bill:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    # Run basic power bill calculator
    calculate_power_bill()
    
    # Run power bill calculator with tax
    calculate_power_bill_with_tax()
