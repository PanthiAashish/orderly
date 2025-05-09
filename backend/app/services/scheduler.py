from apscheduler.schedulers.background import BackgroundScheduler
from app.services.robinhood import execute_trade
from app.db.trade_queue import get_all_trades
import random

scheduler = BackgroundScheduler()

def fetch_price(ticker: str) -> float:
    return round(random.uniform(80, 300), 2)

def check_trades():
    trades = get_all_trades()
    print("⏳ Checking trades...")
    for trade in trades:
        ticker = trade["ticker"]
        amount = trade["amount"]  # 💵 Use amount now
        condition = trade["condition"]
        price = fetch_price(ticker)

        quantity = amount / price  # ➗ Calculate fractional quantity

        if quantity < 0.0001:
            print(f"Skipped {ticker} — quantity too small at current price ${price}")
            continue

        # Make 'price' available for eval
        try:
            if eval(condition):
                print(f"Condition met: {trade['action']} {quantity:.5f} shares of {ticker} at ${price}")

                # Execute fractional trade
                result = execute_trade(trade["action"], ticker, quantity)
                print("Trade executed:", result)
            else:
                print(f"Condition not met for {ticker} (price ${price})")
        except Exception as e:
            print(f"Error evaluating condition: {e}")


def start_scheduler():
    scheduler.add_job(check_trades, "interval", seconds=30)
    scheduler.start()
