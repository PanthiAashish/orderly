# In-memory list to store trade orders
trade_queue = []

def add_trade(trade: dict):
    trade_queue.append(trade)

def get_all_trades():
    return trade_queue

def clear_trades():
    trade_queue.clear()

