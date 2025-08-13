# Global dictionary to store user accounts
user_accounts = {}

def register_user():
    """
    Function to register a new user account
    """
    print("=== Account Registration ===")
    
    # Get user input for account creation
    username = input("Enter username for your account: ").strip()
    
    # Check if username already exists
    if username in user_accounts:
        print("Error: Username already exists! Please choose a different username.")
        return False
    
    # Get password for account
    password = input("Enter password for your account: ")
    
    # Store user account credentials
    user_accounts[username] = password
    
    print("Account created successfully!")
    print(f"Username: {username}")
    print("You can now login with your account.")
    return True

def login_user():
    """
    Function to login to existing user account
    """
    print("=== Account Login ===")
    
    # Get login credentials
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ")
    
    # Check if account exists and password matches
    if username in user_accounts and user_accounts[username] == password:
        print("Login successful!")
        print(f"Welcome to your account, {username}!")
        return True
    else:
        print("Invalid username or password.")
        print("Please check your account credentials.")
        return False

# Main execution for account management
if __name__ == "__main__":
    while True:
        print("\n=== Account Management System ===")
        print("1. Create Account")
        print("2. Login to Account")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Thank you for using Account Management System!")
            break
        else:
            print("Invalid choice! Please try again.")
