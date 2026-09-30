# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}

portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:")
print(", ".join(stock_prices.keys()))

while True:

    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    # Check whether stock exists
    if stock not in stock_prices:
        print("Stock not found.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    # Add stock to portfolio
    portfolio[stock] = portfolio.get(stock, 0) + quantity


# Calculate total investment
total_value = 0

print("\n===== PORTFOLIO SUMMARY =====")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    value = price * quantity

    total_value += value

    print(
        stock,
        ":",
        quantity,
        "shares x $",
        price,
        "=",
        "$",
        value
    )

print("\nTotal Investment Value: $", total_value)


# Optional file saving
save = input("\nSave result to a file? (yes/no): ").lower()

if save == "yes":

    with open("portfolio.txt", "w") as file:

        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=======================\n")

        for stock, quantity in portfolio.items():

            price = stock_prices[stock]
            value = price * quantity

            file.write(
                f"{stock}: {quantity} shares x "
                f"${price} = ${value}\n"
            )

        file.write(
            f"\nTotal Investment Value: ${total_value}\n"
        )

    print("Portfolio saved to portfolio.txt")