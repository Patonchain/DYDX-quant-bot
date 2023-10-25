from func_utils import format_number
from datetime import datetime,timedelta
from pprint import pprint
import time

# GET EXISTING OPEN POSITIONS
def is_open_positions(client, market):

    # PRODUCTIVITY JOINT
    time.sleep(0.5)

    # QUERY POSITION DATA
    all_positions = client.private.get_positions(
        market = market,
        status = "OPEN",
    )

    # DETERMINE OPEN POSITIONS
    if len(all_positions.data["positions"]) > 0:
        return True
    else:
        return False


# CHECK ORDER STATUS
def check_order_status(client, order_id):
    order = client.private.get_order_by_id(order_id)
    if order.data:
        if "order" in order.data.keys():
            return order.data["order"]["status"]
    return "FAILED"

# PLACE MARKET ORDER
def place_market_order(client,market,side,size,price,reduce_only):
    # Get Position ID
    account_response = client.private.get_account()
    position_id = account_response.data["account"]["positionId"]

    # Get Expiration Time
    server_time = client.public.get_time()
    expiration = datetime.fromisoformat(server_time.data["iso"].replace("Z", "")) + timedelta(seconds=70)

    # PLACE AN ORDER
    placed_order = client.private.create_order(
        position_id = position_id,
        market = market,
        side = side,
        order_type = "MARKET",
        post_only = False,
        size = size,
        price = price,
        limit_fee = '0.015',
        expiration_epoch_seconds=expiration.timestamp(),
        time_in_force = "FOK",
        reduce_only = reduce_only
)
    # RETURN RESULT
    return placed_order.data

# ABORT ALL POSITIONS
def abort_all_positions(client):
    
    # CANCEL OPEN ORDERS
    client.private.cancel_all_orders()
    print("STEP1")

    # QUICK CAT NAP
    time.sleep(0.5)
    
    # GET MARKETS FOR REFERENCE OF TICK SIZE
    markets = client.public.get_markets().data
    print("get market data")
    # SNOOZE BUTTON
    time.sleep(0.5)

    # GET ALL OPEN POSITION
    positions = client.private.get_positions(status = "OPEN")
    all_positions = positions.data["positions"]
    print("get open positions")
   
    # HANDLE OPEN POSITIONS
    close_orders = []
    if len(all_positions) > 0:
        print("try closing orders")    
        # LOOP THROUGH POSITIONS
        for position in all_positions:
            
            # DETERMINE THE MARKET
            market = position["market"]
            print("closing one by one")
            # DETERMINE THE SIDE
            side = "BUY"
            if position["side"] == "LONG":
                side = "SELL"
            
            # DETERMINE PRICE
            price = float(position["entryPrice"])
            accept_price = price * 1.7 if side == "BUY" else price * 0.3
            tick_size = markets["markets"][market]["tickSize"] 
            accept_price = format_number(accept_price, tick_size)

            # PLACE ORDER TO CLOSE
            order = place_market_order(
                client,
                market,
                side,
                position["sumOpen"],
                accept_price,
                True
            )
            print("placing order")
            # APPEND THE RESULT
            close_orders.append(order)

            # API FEELING OVER WORKED
            time.sleep(0.2)
        
        # RETURN CLOSED ORDERS
        return close_orders