def cm_to_inches(cm):
    return cm / 2.54

cm = float(input("Enter length in centimeters: "))
inches = cm_to_inches(cm)
print(f"{cm} centimeters is equal to {inches} inches.")