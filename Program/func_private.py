from func_utils import format_number
from datetime import datetime,timedelta
from pprint import pprint
import time

# PLACE MARKET ORDER
def place_market_order(client,market,side,size,price,reduce_only):
    # Get Position ID
    account_response = client.private.get_account()
    position_id = account_response.data["account"]["positionId"]

    # Get Expiration Time
    server_time = client.public.get_time()
    expiration = datetime.fromisoformat(server_time.data["iso"].replace("Z", "")) + timedelta(seconds=70)


# Place an Order
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
    # Return Result
    return placed_order.data

# ABORT ALL POSITIONS
def abort_all_positions(client):
    
    # CANCEL OPEN ORDERS
    client.private.cancel_all_orders()

    # PROTECT API
    time.sleep(0.5)
    
    # GET MARKETS FOR REFERENCE OF TICK SIZE
    markets = client.public.get_markets().data

    # PROTECT API
    time.sleep(0.5)

    # GET ALL OPEN POSITION
    positions = client.private.get_positions(status = "OPEN")
    all_positions = positions.data("positions")

    # HANDLE OPEN POSITIONS
    close_orders = []
    if len(all_positions) > 0:
        
        # LOOP THROUGH POSITIONS
        for position in all_positions:
            
            # DETERMINE THE MARKET
            market = position(market)
            
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

            # APPEND THE RESULT
            close_orders.append(order)

            # API NAP
            time.sleep(0.2)
        
        # RETURN CLOSED ORDERS
        return close_orders