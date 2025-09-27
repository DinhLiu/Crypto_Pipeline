from binance.spot import Spot
from config import BINANCE_API_KEY, BINANCE_API_SECRET
import pandas as pd
from config import SYMBOLS

def get_price(interval="5m", limit=100):
    all_data = []
    client = Spot(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)
    for symbol in SYMBOLS:
        symbol = symbol.upper() #uppercase
        data = client.klines(symbol, interval=interval, limit=limit)
        df = pd.DataFrame(data, columns=[
            "open_time", "open", "high", "low", "close", "volume",
            "close_time", "qav", "num_trades", "taker_base_vol",
            "taker_quote_vol", "ignore"
        ])
        df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
        df["close_time"] = pd.to_datetime(df["close_time"], unit="ms")
        df["symbol"] = symbol   # Adding 'coin' column
        all_data.append(df[["symbol", "open_time", "open", "high", "low", "close", "volume"]])
    return pd.concat(all_data, ignore_index=True)
