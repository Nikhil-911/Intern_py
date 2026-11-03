"""

Stock Portfolio Tracker

"""

import csv
import os

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145,
    "NVDA": 480,
    "META": 320,
    "NFLX": 410,
}


def read_portfolio():
    """Collect stock names and quantities from the user. Returns a dict {symbol: qty}."""
    portfolio = {}
    print("Enter your stocks one by one (type 'done' when finished).")
    print(f"Available stocks: {', '.join(STOCK_PRICES)}\n")

    while True:
        symbol = input("Stock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' is not in our price list. Try again.")
            continue

        qty_raw = input(f"  Quantity of {symbol}: ").strip()
        try:
            qty = int(qty_raw)
        except ValueError:
            print("  Quantity must be a whole number. Try again.")
            continue

        if qty <= 0:
            print("  Quantity must be positive. Try again.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + qty
        print(f"  Added {qty} x {symbol} @ ${STOCK_PRICES[symbol]:,} each.\n")

    return portfolio


def show_summary(portfolio):
    """Print a per-stock breakdown and the total investment value."""
    print("\n" + "=" * 40)
    print("PORTFOLIO SUMMARY")
    print("=" * 40)

    total = 0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"{symbol:<8} {qty:>5} x ${price:>7,} = ${value:>10,}")

    print("-" * 40)
    print(f"{'TOTAL INVESTMENT':<24} = ${total:>10,}")
    print("=" * 40)
    return total


def save_result(portfolio, total, path):
    """Save the summary to a .csv (per-stock rows) or .txt (plain text) file."""
    ext = os.path.splitext(path)[1].lower()

    if ext == ".csv":
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for symbol, qty in portfolio.items():
                price = STOCK_PRICES[symbol]
                writer.writerow([symbol, qty, price, price * qty])
            writer.writerow(["TOTAL", "", "", total])
    else:  # default to plain text
        with open(path, "w") as f:
            f.write("PORTFOLIO SUMMARY\n" + "=" * 30 + "\n")
            for symbol, qty in portfolio.items():
                price = STOCK_PRICES[symbol]
                f.write(f"{symbol}: {qty} x ${price} = ${price * qty}\n")
            f.write(f"TOTAL INVESTMENT: ${total}\n")

    print(f"Result saved to '{path}'.")


def main():
    portfolio = read_portfolio()

    if not portfolio:
        print("No stocks entered. Nothing to calculate.")
        return

    total = show_summary(portfolio)

    choice = input("\nSave the result? (txt / csv / no): ").strip().lower()
    if choice == "txt":
        save_result(portfolio, total, "portfolio_summary.txt")
    elif choice == "csv":
        save_result(portfolio, total, "portfolio_summary.csv")


if __name__ == "__main__":
    main()