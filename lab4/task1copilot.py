# Function to check if a given year is a leap year
def is_leap_year(year):
	"""Return True if the given year is a leap year, else False."""
	if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		return True
	else:
		return False

if __name__ == "__main__":
	try:
		year = int(input("Enter a year: "))
		if is_leap_year(year):
			print(f"{year} is a leap year.")
		else:
			print(f"{year} is not a leap year.")
	except ValueError:
		print("Invalid input. Please enter a valid year.")
