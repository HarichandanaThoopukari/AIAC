
# Function to format full name as "Last First"
def format_full_name(full_name):
    """Return the full name formatted as 'Last First' with proper capitalization."""
    parts = full_name.strip().split()
    if len(parts) < 2:
        return "Invalid input. Please enter both first and last name."
    first = parts[0].capitalize()
    last = parts[-1].capitalize()
    return f"{last} {first}"

if __name__ == "__main__":
    full_name = input("Enter full name (first last): ")
    formatted = format_full_name(full_name)
    print(f"Formatted name: {formatted}")
