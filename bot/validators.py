
def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side, It should be BUY or SELL")
    return True

def validate_type(type):
    if type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Invalid type, It should be MARKET, LIMIT, or STOP")
    return True

def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Invalid quantity, It should be greater than 0")
    return True

def validate_price(price):
    if price <= 0:
        raise ValueError("Invalid price, It should be greater than 0")
    return True

def validate_order(order):

    if order["type"] == "LIMIT":
        validate_price(order["price"])
    elif order["type"] == "STOP":
        validate_price(order["price"])
        validate_price(order["stop_price"])
    validate_side(order["side"])
    validate_type(order["type"])
    validate_quantity(order["quantity"])
    return True