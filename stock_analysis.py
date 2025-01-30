import yfinance as yf
import pandas as pd
import ta  # For technical analysis
import matplotlib.pyplot as plt

def fetch_stock_data(stock_symbol, start="2023-01-01", end="2025-01-01"):
    """Fetch historical stock data from Yahoo Finance."""
    df = yf.download(stock_symbol, start=start, end=end)
    df.to_csv(f"data/{stock_symbol}.csv")  # Save for later use
    return df

def apply_indicators(df):
    """Apply SMA, EMA, RSI, and MACD indicators to stock data."""
    df['SMA50'] = df['Close'].rolling(window=50).mean()
    df['SMA200'] = df['Close'].rolling(window=200).mean()
    df['EMA50'] = df['Close'].ewm(span=50, adjust=False).mean()
    
    # Ensure the Close column is a 1D Series before passing to RSIIndicator
    df['RSI'] = ta.momentum.RSIIndicator(df['Close'].squeeze(), window=14).rsi()
    
    # MACD (Moving Average Convergence Divergence)
    macd = ta.trend.MACD(df['Close'].squeeze())  # Ensure it's 1D
    df['MACD'] = macd.macd()
    df['Signal_Line'] = macd.macd_signal()
    
    return df

def generate_signals(df):
    """Generate buy and sell signals based on SMA and RSI."""
    df['Buy_Signal'] = (df['SMA50'] > df['SMA200']) & (df['RSI'] < 30)
    df['Sell_Signal'] = (df['SMA50'] < df['SMA200']) & (df['RSI'] > 70)
    return df

def plot_stock_data(df, stock_symbol):
    """Plot stock prices with SMA and buy/sell signals."""
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['Close'], label="Close Price", color='blue')
    plt.plot(df.index, df['SMA50'], label="50-day SMA", color='green')
    plt.plot(df.index, df['SMA200'], label="200-day SMA", color='red')

    # Ensure markers are plotted even if only a few exist
    if df['Buy_Signal'].sum() > 0:
        plt.scatter(df.index[df['Buy_Signal']], df['Close'][df['Buy_Signal']], 
                    marker="^", color='green', label="Buy Signal", alpha=1, s=100)
    
    if df['Sell_Signal'].sum() > 0:
        plt.scatter(df.index[df['Sell_Signal']], df['Close'][df['Sell_Signal']], 
                    marker="v", color='red', label="Sell Signal", alpha=1, s=100)

    plt.legend()
    plt.title(f"{stock_symbol} Price Chart")
    plt.show()

