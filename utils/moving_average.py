# utils/moving_average.py

def calculate_moving_average(price_history: dict, days: int) -> float:
    sorted_dates = sorted(price_history.keys(), reverse=True)
    selected_prices = [price_history[date] for date in sorted_dates[:days]]
    if not selected_prices:
        return 0
    return sum(selected_prices) / len(selected_prices)
