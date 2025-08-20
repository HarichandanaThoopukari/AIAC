def collect_user_data():
    # Prompt the user to enter their name
    name = input("Enter your name: ")
    # Prompt the user to enter their age
    age = input("Enter your age: ")
    # Prompt the user to enter their email
    email = input("Enter your email: ")
    
    # NOTE: Protect user data by not sharing or storing it insecurely.
    # Do not print, log, or transmit sensitive information unless necessary and secure.
    # If storing data, use secure storage and follow privacy best practices.
    
    # Display the collected user data
    print("\nUser Data Collected:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")

# Run the function if this script is executed directly
if __name__ == "__main__":
    collect_user_data()