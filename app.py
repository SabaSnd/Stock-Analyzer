import streamlit as st
import pandas as pd
from stock_analysis import fetch_stock_data, apply_indicators, generate_signals, plot_stock_data

st.title("📈 Smart Stock Analyzer")

stock_symbol = st.text_input("Enter Stock Symbol", "AAPL")

if st.button("Analyze"):
    df = fetch_stock_data(stock_symbol)
    df = apply_indicators(df)
    df = generate_signals(df)
    
    st.write(df.tail())  # Show last few rows
    plot_stock_data(df, stock_symbol)  # Show plot
