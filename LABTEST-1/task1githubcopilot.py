# Currency converter using exchange rates stored in a dictionary

# Example exchange rates (relative to USD)
exchange_rates = {
    'USD': 1.0,
    'INR': 72.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'JPY': 110.0
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Unsupported currency.")
    # Convert amount to USD first, then to target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return converted_amount

if __name__ == "__main__":
    print("Available currencies:", ', '.join(exchange_rates.keys()))
    from_curr = input("Enter source currency code: ").upper()
    to_curr = input("Enter target currency code: ").upper()
    amount = float(input(f"Enter amount in {from_curr}: "))
    try:
        result = convert_currency(amount, from_curr, to_curr)
        print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
    except ValueError as e:
        print(e)