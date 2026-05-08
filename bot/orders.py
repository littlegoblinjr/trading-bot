from bot.client import client
import logging

def create_order(symbol, side, typee, quantity, price=None, stop_price=None):

    try:

        if typee == "LIMIT":
            logging.info(
                    f"Creating {typee} order | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price}"
                )
        elif typee == "STOP":
            logging.info(
                f"Creating {typee} order | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price} | Stop Price={stop_price}"
            )
        else:
            logging.info(
                f"Creating {typee} order | Symbol={symbol} | Side={side} | Quantity={quantity}"
            )


        params = {
            "symbol": symbol,
            "side": side,
            "type": typee,
            "quantity": quantity,
        }

        if typee == "LIMIT":
            params["timeInForce"] = "GTC"
            params["price"] = price

        if typee == "STOP":
            params["price"] = price
            params["stopPrice"] = stop_price
            params["timeInForce"] = "GTC"

        order = client.futures_create_order(
            **params
        )

        if typee == "LIMIT":
            logging.info(f"Created {typee} order | ID={order.get('orderId')} | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price}")
        elif typee == "STOP":
            logging.info(f"Created {typee} order | ID={order.get('orderId')} | Symbol={symbol} | Side={side} | Quantity={quantity} | Stop Price={stop_price}")
        else:
            logging.info(f"Created {typee} order | ID={order.get('orderId')} | Symbol={symbol} | Side={side} | Quantity={quantity}")
        return order

    except Exception as e:
        if typee == "LIMIT":
            logging.error(f"Error creating order | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price} | Error={e}")
        elif typee == "STOP":
            logging.error(f"Error creating order | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price} | Stop Price={stop_price} | Error={e}")
        else:
            logging.error(f"Error creating order | Symbol={symbol} | Side={side} | Quantity={quantity} | Error={e}")
        return None

