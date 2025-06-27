# services/chart_service.py

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from io import BytesIO
from datetime import datetime


def create_price_chart(history: dict, symbol: str) -> BytesIO:
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in sorted(history.keys())]
    prices = [history[d.strftime("%Y-%m-%d")] for d in dates]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, label=f"{symbol.upper()} Price", color="orange")
    plt.title(f"{symbol.upper()} Price Chart (Last {len(dates)} Days)")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.gcf().autofmt_xdate()

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    return buffer
