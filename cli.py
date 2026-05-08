import bot.logging_config
from bot.client import client
from bot.orders import create_order
from bot.validators import (validate_order,
                            validate_side,
                            validate_type,
                            validate_quantity,
                            validate_price)



symbol = input("Enter the Symbol please: ")
side = input("Enter the Side please (BUY/SELL): ").upper()
typee = input("Enter the Type please (MARKET/LIMIT/STOP): ").upper()
quantity = float(input("Enter the Quantity (e.g. 0.002 for >100 USDT notional): "))

if typee == "LIMIT":
    price = float(input("Enter the Price please: "))
elif typee == "STOP":
    stop_price = float(input("Enter the Stop Price please: "))
    price = float(input("Enter the Price please: "))
else:
    price = None

print("========== ORDER REQUEST ==========")
print(f"Symbol: {symbol}")
print(f"Side: {side}")
print(f"Type: {typee}")
print(f"Quantity: {quantity}")
if price:
    print(f"Price: {price}")
    print(f"Estimated Notional: {quantity * price:.2f} USDT")
if typee == "STOP":
    print(f"Stop Price: {stop_price}")
print("===================================")


try:

    if typee == "LIMIT":
        validate_order({
            "symbol": symbol,
            "side": side,
            "type": typee,
            "quantity": quantity,
            "price": price
        })
    elif typee == "STOP":
        validate_order({
            "symbol": symbol,
            "side": side,
            "type": typee,
            "quantity": quantity,
            "stop_price": stop_price,
            "price": price
        })
    else:
        validate_order({
            "symbol": symbol,
            "side": side,
            "type": typee,
            "quantity": quantity
        })
except ValueError as e:
    print(f"Error: {e}")


try:

    if typee == "LIMIT":
        response = create_order(
            symbol=symbol,
            side=side,
            typee=typee,
            quantity=quantity,
            price=price
        )
    elif typee == "STOP":
        response = create_order(
            symbol=symbol,
            side=side,
            typee=typee,
            quantity=quantity,
            stop_price=stop_price,
            price=price
        )
    else:
        response = create_order(
            symbol=symbol,
            side=side,
            typee=typee,
            quantity=quantity
        )

    if response:

        print("\n========== ORDER RESPONSE ==========")

        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Quantity: {response.get('executedQty')}")

        avg_price = response.get("avgPrice")

        if avg_price:
            print(f"Average Price: {avg_price}")

        print("====================================")

        print("Order placed successfully!")

    else:

        print("Order failed!")


except Exception as e:
    print(f"Error: {e}")





