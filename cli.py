import argparse
import sys
import bot.logging_config
from bot.orders import create_order
from bot.validators import validate_order

def main():
    parser = argparse.ArgumentParser(description="PrimaTrade Binance Futures CLI Bot")
    
    # Optional arguments - if not provided, we will prompt the user
    parser.add_argument("--symbol", help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", choices=["MARKET", "LIMIT", "STOP"], help="Order type")
    parser.add_argument("--quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit price (required for LIMIT/STOP)")
    parser.add_argument("--stop_price", type=float, help="Stop price (required for STOP)")

    args = parser.parse_args()

    # If no arguments provided, use interactive prompts (Enhanced UX)
    symbol = args.symbol or input("Enter the Symbol (e.g., BTCUSDT): ").upper()
    side = args.side or input("Enter the Side (BUY/SELL): ").upper()
    typee = args.type or input("Enter the Type (MARKET/LIMIT/STOP): ").upper()
    quantity = args.quantity or float(input("Enter the Quantity: "))
    
    price = args.price
    stop_price = args.stop_price

    if typee == "LIMIT" and not price:
        price = float(input("Enter the Limit Price: "))
    elif typee == "STOP":
        if not stop_price:
            stop_price = float(input("Enter the Stop Price: "))
        if not price:
            price = float(input("Enter the Limit Price for the Stop: "))

    print("\n========== ORDER REQUEST ==========")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {typee}")
    print(f"Quantity: {quantity}")
    if price: print(f"Price: {price}")
    if stop_price: print(f"Stop Price: {stop_price}")
    print("===================================\n")

    # Validation
    try:
        order_data = {
            "symbol": symbol,
            "side": side,
            "type": typee,
            "quantity": quantity,
            "price": price,
            "stop_price": stop_price
        }
        validate_order(order_data)
    except ValueError as e:
        print(f"Validation Error: {e}")
        sys.exit(1)

    # Execution
    try:
        response = create_order(
            symbol=symbol,
            side=side,
            typee=typee,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        if response:
            print("========== ORDER RESPONSE ==========")
            print(f"Order ID: {response.get('orderId')}")
            print(f"Status: {response.get('status')}")
            print(f"Executed Qty: {response.get('executedQty')}")
            if response.get('avgPrice'):
                print(f"Avg Price: {response.get('avgPrice')}")
            print("====================================")
            print("SUCCESS: Order placed successfully!")
        else:
            print("FAILURE: Order failed at exchange (check logs for details).")

    except Exception as e:
        print(f"Critical Error: {e}")

if __name__ == "__main__":
    main()
