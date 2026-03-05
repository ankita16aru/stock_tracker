import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# Stock and index
stock = "ADANIPORTS.NS"
nifty = "^NSEI"

# Fetch prices
stock_price = yf.Ticker(stock).history(period="1d")["Close"].iloc[-1]
nifty_price = yf.Ticker(nifty).history(period="1d")["Close"].iloc[-1]

today = datetime.now().strftime("%Y-%m-%d")

data = {
    "Date": [today],
    "AdaniPorts": [stock_price],
    "NIFTY50": [nifty_price]
}

df = pd.DataFrame(data)

file = "data.csv"

# Append data
if os.path.exists(file):
    old = pd.read_csv(file)
    df = pd.concat([old, df], ignore_index=True)

df.to_csv(file, index=False)

print("Updated:", today, stock_price, nifty_price)