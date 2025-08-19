def count_lines_in_file(filename):
    """
    Read a text file and return the number of lines.
    
    Args:
        filename (str): Name of the file to read
        
    Returns:
        int: Number of lines in the file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1
    except Exception as e:
        print(f"Error reading file: {e}")
        return -1


def display_file_content(filename):
    """
    Display the content of a file with line numbers.
    
    Args:
        filename (str): Name of the file to display
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            print(f"Content of {filename}:")
            print("-" * 40)
            for i, line in enumerate(lines, 1):
                print(f"Line {i}: {line.strip()}")
            print("-" * 40)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
def main():
    """Main function to demonstrate line counting with example and file reading."""
    print("File Line Counter")
    print("=" * 40)
    # Show example
    print("Example:")
    example_lines = [
        "hello sr university.hanmakonda warangal.",
        "Top engineering college.",
        "Offers wide variety of courses."
    ]
    print("Content:")
    for i, line in enumerate(example_lines, 1):
        print(f"Line {i}: {line}")
    
    print(f"No.of lines in a.txt = {len(example_lines)}.")
    print("\n" + "=" * 40)

    # Read actual a.txt file
    filename = "a.txt"
    line_count = count_lines_in_file(filename)
    
    if line_count >= 0:
        print(f"Reading file: {filename}")
        display_file_content(filename)
        print(f"No.of lines in {filename} = {line_count}.")
    else:
        print("Could not read the file.")
if __name__ == "__main__":
    main()
