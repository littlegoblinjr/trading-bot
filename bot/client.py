import os
from binance.client import Client
from dotenv import load_dotenv
import time

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
secret_key = os.getenv("BINANCE_SECRET_KEY")

# Initialize the client
client = Client(api_key, secret_key)

# The task specifically requested this URL for all API interactions
# For python-binance, we point the Futures API to the testnet endpoint
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# Synchronization with server time (crucial for API calls to succeed)
try:
    server_time = client.get_server_time()
    client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)
except Exception:
    # Fallback if connection fails during init
    client.timestamp_offset = 0