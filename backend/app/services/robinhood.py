import robin_stocks.robinhood as r
from app.core.config import settings

def login_to_robinhood():
    try:
        print("Attempting login...")
        r.login(
            username=settings.ROBINHOOD_USERNAME,
            password=settings.ROBINHOOD_PASSWORD,
            store_session=True
        )
        print("Login successful. Approve in app if needed.")
    except Exception as e:
        print("Login failed:", e)
        raise


def execute_trade(action, ticker, quantity):
    quantity = round(quantity, 6)

    if action == "buy":
        return r.orders.order_buy_fractional_by_quantity(ticker, quantity)
    elif action == "sell":
        return r.orders.order_sell_fractional_by_quantity(ticker, quantity)
    else:
        raise ValueError("Unsupported trade action.")

def get_account_info():
    return r.account.get_account_info()

