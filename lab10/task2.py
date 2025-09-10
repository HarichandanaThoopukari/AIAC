# Function to find common elements in two lists
# Simple version using list comprehension
def find_common(a, b):
    return [x for x in a if x in b]

# Optimized version using set intersection
def find_common_optimized(a, b):
    return list(set(a) & set(b))

# Example usage
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

print("Original:", find_common(a, b))
print("Optimized:", find_common_optimized(a, b))