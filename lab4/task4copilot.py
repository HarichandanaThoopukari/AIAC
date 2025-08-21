def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
print(f"Number of vowels: {vowel_count}")