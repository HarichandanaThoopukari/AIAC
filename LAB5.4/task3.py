# Product Recommendation System with Transparency and Fairness

# Sample product catalog
products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Smartwatch",
    "Tablet",
    "Camera",
    "Bluetooth Speaker",
    "E-reader"
]

# Collect user purchase/view history
print("Available products:")
for idx, product in enumerate(products):
    print(f"{idx + 1}. {product}")

# Ask user to input previously purchased/viewed products
user_history = input("Enter the numbers of products you've purchased/viewed (comma separated): ")
user_indices = [int(i.strip()) - 1 for i in user_history.split(",") if i.strip().isdigit()]

# Ensure fairness: recommend products not already in user's history
# Transparency: explain recommendation logic in comments
recommended = []
for idx, product in enumerate(products):
    if idx not in user_indices:
        recommended.append(product)

# Show recommendations
print("\nRecommended products for you (excluding those you've already interacted with):")
for product in recommended:
    print("-", product)

# Note:
# - Recommendations are based on excluding products the user already knows.
# - No bias towards any product; all unseen products are recommended equally.
# - User input is used only for matching, not for profiling or discrimination.