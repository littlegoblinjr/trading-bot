# 🚀 Binance Futures Trading Bot (Testnet)

This application is a professional trading bot built for the **Binance Futures Testnet (USDT-M)**. It supports Market, Limit, and Stop orders with robust validation, logging, and error handling.

---

## 📋 Task Deliverables Status

- [x] **Core Requirements**: All met (Market/Limit orders, BUY/SELL, CLI UX).
- [x] **Logging**: Fully implemented (API requests, responses, and errors saved to `bot/logs/trading.log`).
- [x] **Validation**: Input and Notional value validation included.
- [x] **Bonus Feature 1**: Added **STOP** order type support.
- [x] **Bonus Feature 2**: Enhanced **CLI UX** with interactive prompts.
- [x] **Bonus Feature 3**: Added a **Glassmorphic React Dashboard**.

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- Python 3.11+
- Node.js 20+ (optional, for Dashboard)
- Binance Futures Testnet API Key & Secret ([Get it here](https://testnet.binancefuture.com/))

### 2. Installation
```bash
# Clone and enter the project
git clone https://github.com/littlegoblinjr/trading-bot.git
cd trading-bot

# Install backend dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
BINANCE_API_KEY=your_testnet_key_here
BINANCE_SECRET_KEY=your_testnet_secret_here
```

---

## 📖 How to Run Examples

### 1. Terminal Interface (Standard & Argparse)
The CLI tool supports both direct command-line arguments (using `argparse`) and interactive prompts.

**Option A: Direct Command (Professional Mode)**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Option B: Interactive Prompts (Enhanced UX)**
```bash
python cli.py
```
(Simply run the command and it will guide you through the parameters).

### 2. Modern Dashboard (Bonus)
If you wish to use the graphical interface:
```bash
# Start the FastAPI Backend
python app.py

# In a new terminal, start the React Frontend
cd frontend
npm install
npm run dev
```

---

## 📁 Project Structure
Following the suggested task architecture:
```text
trading_bot/
  bot/
    client.py        # Binance API client setup (configured for Testnet)
    orders.py        # Order placement logic
    validators.py    # Input and exchange parameter validation
    logging_config.py # Centralized logging settings
    logs/            # Log files storage
  frontend/          # React Dashboard (Bonus)
  cli.py             # Main CLI entry point
  app.py             # FastAPI Web Engine
  requirements.txt
```

---

## 🧠 Assumptions
1. **Trading Pair**: The bot assumes the user is trading **USDT-M** pairs (e.g., BTCUSDT).
2. **Minimum Notional**: Binance Futures typically requires a minimum notional value (e.g., >100 USDT). The bot provides warnings if the calculated notional is too low.
3. **Environment**: The bot defaults to the **Binance Futures Testnet** URL as specified in the task instructions (`https://testnet.binancefuture.com/fapi`).

---

## 📝 Logging
All interactions are logged with timestamps and details in:
`bot/logs/trading.log`
