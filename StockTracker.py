import requests

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.stocks = {}

    def add_stock(self, symbol, shares):
        if symbol in self.stocks:
            self.stocks[symbol]["shares"] += shares
        else:
            self.stocks[symbol] = {"shares": shares, "price": None}
        self.update_stock_price(symbol)

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"{symbol} removed from the portfolio.")
        else:
            print(f"{symbol} not found in the portfolio.")

    def update_stock_price(self, symbol):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        if "Global Quote" in data:
            price = float(data["Global Quote"]["05. price"])
            self.stocks[symbol]["price"] = price
        else:
            print(f"Failed to fetch data for {symbol}")

    def portfolio_value(self):
        total_value = 0
        for symbol, data in self.stocks.items():
            if data["price"] is not None:
                total_value += data["shares"] * data["price"]
        return total_value

    def display_portfolio(self):
        print("Stock Portfolio:")
        for symbol, data in self.stocks.items():
            if data["price"] is not None:
                print(f"{symbol}: {data['shares']} shares, Current Price: ${data['price']:.2f}")
            else:
                print(f"{symbol}: {data['shares']} shares, Current Price: Not available")

# Main Program
api_key = "1CRIK8MBKWTO34DO"  # Replace with your Alpha Vantage API key
portfolio = StockPortfolio(api_key)

while True:
    print("\nOptions:")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. View Portfolio")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        symbol = input("Enter stock symbol: ").upper()
        shares = int(input("Enter number of shares: "))
        portfolio.add_stock(symbol, shares)
    elif choice == "2":
        symbol = input("Enter stock symbol to remove: ").upper()
        portfolio.remove_stock(symbol)
    elif choice == "3":
        portfolio.display_portfolio()
        print(f"Total Portfolio Value: ${portfolio.portfolio_value():.2f}")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
