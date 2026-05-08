from bot.client import futures_client
import logging

def get_account_summary():
    """Fetches real account balance and unrealized PnL from Binance Futures."""
    try:
        account_info = futures_client.futures_account()
        
        # Get total wallet balance in USDT
        total_balance = "0.00"
        for asset in account_info.get('assets', []):
            if asset['asset'] == 'USDT':
                total_balance = asset['walletBalance']
                break
        
        # Get total unrealized PnL
        unrealized_pnl = account_info.get('totalUnrealizedProfit', '0.00')
        
        return {
            "balance": float(total_balance),
            "pnl": float(unrealized_pnl)
        }
    except Exception as e:
        logging.error(f"Error fetching account info: {e}")
        return {"balance": 0.0, "pnl": 0.0}
