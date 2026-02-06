# 📈 Stock Portfolio Tracker

A powerful yet simple Command Line Interface (CLI) tool to track your stock investments and calculate your portfolio value with ease.

![Stock Tracker Logo](https://img.shields.io/badge/Version-2.0-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)

---

## 🌟 Features

- **Animated Startup**: A professional ASCII art logo with loading animations to set the mood!
- **Core Market Data**: Includes a pre-defined database of popular stocks like AAPL, TSLA, GOOGL, and more.
- **Easy Portfolio Input**: Simple prompt-based input for adding your stock holdings and quantities.
- **Detailed Calculations**: Instantly calculates individual stock values and your total investment value.
- **Professional Reports**: Generates a clean, formatted table in the console for easy reading.
- **Export to CSV**: Save your portfolio data to a `portfolio_report.csv` file for external tracking and spreadsheets.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone or download the repository to your local machine.
2. Ensure you have the following files in the project folder:
   - `stock_tracker.py`

### Running the Tracker
Open your terminal or command prompt, navigate to the project directory, and run:
```bash
python stock_tracker.py
```

---

## 📖 How to Use

1. **Launch**: Start the script and enjoy the animated intro!
2. **Input Holdings**: 
   - Enter the stock symbol (e.g., `AAPL`).
   - Enter the quantity you own.
   - Type `DONE` when you have finished adding all your stocks.
3. **Review Report**: The program will display a formatted table of your portfolio.
4. **Save Data**: When prompted, type `y` to export your report to a CSV file.

---

## 📂 Project Structure

- `stock_tracker.py`: The main Python script containing all logic and UI.
- `portfolio_report.csv`: (Generated) The exported portfolio data.
- `README.md`: This file!

---

## 📊 Available Stocks
Currently supported stocks out of the box:
- **AAPL** (Apple)
- **TSLA** (Tesla)
- **GOOGL** (Alphabet)
- **MSFT** (Microsoft)
- **AMZN** (Amazon)
- **NVDA** (NVIDIA)

---

> [!NOTE]
> This tracker currently uses a hardcoded database for stock prices. Future versions may include real-time API integration!
