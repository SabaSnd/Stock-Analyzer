# 📈 Smart Stock Analyzer

## 📌 Overview
Smart Stock Analyzer is a Python-based stock analysis tool that fetches real-time stock data and applies various technical indicators to help determine **buy/sell signals** based on **SMA, RSI, and MACD**. The tool uses **Yahoo Finance API** to retrieve stock prices and plots a chart with insights for traders.

## 🚀 Features
- 📊 **Fetches stock data** from Yahoo Finance
- 📈 **Applies technical indicators** (SMA, EMA, RSI, MACD)
- ✅ **Generates Buy/Sell signals**
- 📉 **Visualizes stock trends** using Matplotlib

## 🛠️ Technologies Used
- Python 🐍
- `yfinance` (Yahoo Finance API)
- `pandas` (Data handling)
- `ta` (Technical Analysis Library)
- `matplotlib` (Plotting)

## 📥 Installation
### 1️⃣ Clone the Repository
```bash
 git clone https://github.com/your-username/Stock-Analyzer.git
 cd Stock-Analyzer
```
### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔍 Usage
### 1️⃣ Run the Script
```bash
python app.py
```
### 2️⃣ Example Output
```bash
AAPL Stock Data:
Date          Close   SMA50   SMA200   RSI   MACD   Signal_Line  Buy_Signal  Sell_Signal
2024-12-24   255.49  232.34  211.41   75.75  2.5    2.1          False       True
2024-12-26   258.19  236.33  211.84   76.45  3.1    2.7          False       True
```
### 3️⃣ Visual Output (Plot)
The tool generates a **stock price chart** with:
✅ **Buy Signals** (Green upward arrows)
❌ **Sell Signals** (Red downward arrows)

## ⚙️ How It Works
1. **Fetch stock data** using Yahoo Finance.
2. **Apply technical indicators:**
   - **SMA50 & SMA200**: Moving averages for trend analysis
   - **RSI**: Determines overbought/oversold conditions
   - **MACD**: Identifies momentum trends
3. **Generate Buy/Sell signals:**
   - Buy: `SMA50 > SMA200` & `RSI < 30`
   - Sell: `SMA50 < SMA200` & `RSI > 70`
4. **Plot the data** with trend lines and markers.

## 🛠️ Contribution
Want to improve this tool? Fork the repo and submit a PR! 🚀

## 📝 License
This project is **open-source** under the [MIT License](LICENSE).

---
🔗 **GitHub Repo:** [Your Repo Link Here]

