rates = {
    "USD": 1.0,
    "INR": 83.5,
    "EUR": 0.91,
    "GBP": 0.78,
    "JPY": 143.2
}

amount = float(input("Enter amount: "))
from_currency = input("From (USD/INR/EUR/GBP/JPY): ").upper()
to_currency = input("To (USD/INR/EUR/GBP/JPY): ").upper()

converted = amount / rates[from_currency] * rates[to_currency]

print(f"{amount} {from_currency} = {round(converted, 2)} {to_currency}")
