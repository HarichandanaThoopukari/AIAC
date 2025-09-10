def discount(price, category):
    discount_rules = {
        "student": [(1000, 0.9), (0, 0.95)],
        "regular": [(2000, 0.85), (0, 0.95)],
        "senior": [(1000, 0.88), (0, 0.93)],
        "veteran": [(1000, 0.87), (0, 0.92)],
    }

    if category in discount_rules:
        for threshold, rate in discount_rules[category]:
            if price > threshold:
                return price * rate
    else:
        return price * 0.85 if price > 2000 else price

print(discount(1200, "student"))
print(discount(2500, "regular"))
print(discount(800, "student"))
print(discount(1500, "regular"))
print(discount(1200, "senior"))
print(discount(2500, "veteran"))
print(discount(800, "senior"))
print(discount(1500, "veteran"))