# 🚀 PrimaTrade: Premium Binance Futures Trading Bot

PrimaTrade is a high-performance, containerized trading bot for Binance Futures. It features a professional **Glassmorphic Dashboard** built with React and Tailwind CSS, backed by a robust **FastAPI** backend that integrates directly with the Binance API.

![Dashboard Preview](https://img.shields.io/badge/Dashboard-Premium-00ff88?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Stack-React_|_FastAPI_|_Docker-blue?style=for-the-badge)

## ✨ Features

- **💎 Luxury Dashboard**: Modern glassmorphic interface with real-time feedback.
- **⚡ Execution Support**: Market, Limit, and Stop-Limit orders.
- **📊 Real-time Monitoring**: Live log feed from the trading engine directly to the browser.
- **🛡️ Built-in Validation**: Notional value checks and parameter validation to prevent exchange rejections.
- **🐳 Dockerized**: Seamless deployment using Docker Compose.
- **📝 Logging Engine**: Comprehensive logging for every trade and API interaction.

## 🛠️ Tech Stack

- **Frontend**: React (Vite), Tailwind CSS, Lucide Icons, Axios.
- **Backend**: FastAPI, Uvicorn, Pydantic.
- **Bot Engine**: Python, `python-binance`.
- **Infrastructure**: Docker, Docker Compose.

## 🚀 Getting Started

### Prerequisites

- [Python 3.11+](https://www.python.org/)
- [Node.js 20+](https://nodejs.org/)
- [Docker & Docker Compose](https://www.docker.com/) (Optional but recommended)
- A [Binance API Key/Secret](https://testnet.binancefuture.com/) (Testnet is recommended for testing).

### Installation (Docker - Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/littlegoblinjr/trading-bot.git
   cd trading-bot
   ```

2. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```env
   BINANCE_API_KEY=your_api_key
   BINANCE_SECRET_KEY=your_secret_key
   ```

3. **Launch the stack**:
   ```bash
   docker-compose up --build
   ```

### Manual Installation

#### 1. Backend
```bash
pip install -r requirements.txt
python app.py
```

#### 2. Frontend
```bash
cd frontend
npm install
npm run dev
```

### Terminal CLI Usage
If you prefer to trade directly from your terminal without the dashboard:
```bash
python cli.py
```
This utility will prompt you for the symbol, side, and order parameters sequentially.

## 📁 Project Structure

```text
├── bot/                # Core trading logic
│   ├── logs/           # Persistent log storage
│   ├── orders.py       # Order execution logic
│   ├── validators.py   # Safety & validation checks
│   ├── client.py       # Binance API client setup
│   └── logging_config.py # Shared logging configuration
├── frontend/           # React dashboard code
├── app.py              # FastAPI Web Engine
├── cli.py              # Legacy terminal interface
└── docker-compose.yml  # Multi-container orchestration
```

## ⚠️ Disclaimer

This project is for educational purposes only. Trading cryptocurrencies involves significant risk. Never trade with money you cannot afford to lose. The authors are not responsible for any financial losses incurred using this software.

---

