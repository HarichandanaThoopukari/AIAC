# Program to count number of vowels in a given string

# Read input from the user
input_str = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
vowel_count = sum(1 for char in input_str if char in vowels)

print(f"Vowel count={vowel_count}.")