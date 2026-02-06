# Stock Portfolio Tracker

# Import necessary modules
import csv
import os
import time
import sys

# Print animated logo
def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_stocktracker_logo():
    """Display animated Stock Tracker logo"""
    
    colors = ['\033[96m', '\033[92m', '\033[93m', '\033[94m']
    
    print("Loading Stock Tracker...\n")
    
    # Simple loading animation since frames were empty
    loading_chars = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write(f"\rLoading Market Data... {loading_chars[i % len(loading_chars)]}")
        sys.stdout.flush()
            
    clear_screen()
    # Final logo
    final_logo = """
    \033[92m
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║     ███████╗████████╗ ██████╗  ██████╗██╗  ██╗       ║
    ║     ██╔════╝╚══██╔══╝██╔═══██╗██╔════╝██║ ██╔╝       ║
    ║     ███████╗   ██║   ██║   ██║██║     █████╔╝        ║
    ║     ╚════██║   ██║   ██║   ██║██║     ██╔═██╗        ║
    ║     ███████║   ██║   ╚██████╔╝╚██████╗██║  ██╗       ║
    ║     ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝╚═╝  ╚═╝       ║
    ║                                                      ║
    ║     ████████╗██████╗  █████╗  ██████╗██╗  ██╗        ║
    ║     ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝        ║
    ║        ██║   ██████╔╝███████║██║     █████╔╝         ║
    ║        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗         ║
    ║        ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗        ║
    ║        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝        ║
    ║                                                      ║
    ║          📊 Version 2.0 | Market Ready! 📈          ║
    ║          💰 Your Personal Trading Assistant 💰      ║
    ║                                                      ║
    ╚══════════════════════════════════════════════════════╝
    \033[0m
    """
    print(final_logo)
    print("\n" + "="*60)

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 350.00,
    "AMZN": 130.00,
    "NVDA": 460.00
}

# text color yellow
YELLOW = '\033[93m'
RESET = '\033[0m'

# Function to display available stocks
def display_available_stocks():
    print(f"{YELLOW}\n--- Available Stocks ---{RESET}")
    for stock, price in STOCK_PRICES.items():
        print(f"{YELLOW}{stock}: ${price:.2f}{RESET}")
    print(YELLOW + "------------------------" + RESET)

# Function to get user input for stock holdings
def get_portfolio_input():
    portfolio = {}
    # color text green
    GREEN = '\033[92m'
    print(f"{GREEN}\nEnter your stock holdings. Type 'DONE' when finished.{RESET}")
    
    # Loop to get stock symbols and quantities
    while True:
        symbol = input("Enter Stock Symbol (e.g., AAPL): ").strip().upper()
        if symbol == 'DONE':
            break
        
        if symbol not in STOCK_PRICES:
            print(f"Error: '{symbol}' is not in our database. Available: {', '.join(STOCK_PRICES.keys())}")
            continue
        # Get quantity   
        try:
            quantity_str = input(f"Enter quantity for {symbol}: ").strip()
            quantity = float(quantity_str)
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            
            if symbol in portfolio:
                portfolio[symbol] += quantity
            else:
                portfolio[symbol] = quantity
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            
    return portfolio

# Function to calculate total value of portfolio
def calculate_portfolio(portfolio):
    results = []
    total_investment = 0.0
    
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_investment += value
        results.append({
            "Symbol": symbol,
            "Quantity": quantity,
            "Price": price,
            "Total Value": value
        })
        
    return results, total_investment

# Function to display report
def display_report(results, total_investment):
    print("\n" + "="*40)
    print(f"{'Stock':<10} | {'Qty':<10} | {'Price':<10} | {'Value':<10}")
    print("-" * 46)
    for item in results:
        print(f"{item['Symbol']:<10} | {item['Quantity']:<10.2f} | ${item['Price']:<9.2f} | ${item['Total Value']:<9.2f}")
    print("-" * 46)
    print(f"TOTAL INVESTMENT VALUE: ${total_investment:.2f}")
    print("="*40 + "\n")

# Function to save report to CSV file
def save_to_file(results, total_investment):
    filename = "portfolio_report.csv"
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Symbol", "Quantity", "Price", "Total Value"])
            for item in results:
                writer.writerow([item["Symbol"], item["Quantity"], item["Price"], item["Total Value"]])
            writer.writerow([])
            writer.writerow(["TOTAL", "", "", total_investment])
        print(f"Report saved successfully to '{os.path.abspath(filename)}'")
    except Exception as e:
        print(f"Error saving file: {e}")

# Main function
def main():
    display_stocktracker_logo()
    # color text blue
    print(f"\033[94mWelcome to the Simple Stock Portfolio Tracker\033[0m")
    display_available_stocks()
    
    portfolio = get_portfolio_input()
    
    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    results, total_value = calculate_portfolio(portfolio)
    display_report(results, total_value)
    
    save_choice = input("Do you want to save this report to a CSV file? (y/n): ").strip().lower()
    if save_choice == 'y':
        save_to_file(results, total_value)
    
    print("Thank you for using the Stock Tracker!")
    
    if save_choice == 'y':
        time.sleep(5)
        clear_screen()

if __name__ == "__main__":
    main()