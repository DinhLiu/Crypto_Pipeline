import websocket
import json
import pandas as pd
from datetime import datetime
from UsingWebSocket.load_data import insert_data
from config import SYMBOLS

def on_message(ws, message):
    data = json.loads(message)
    stream = data.get("stream", "")
    payload = data.get("data", {})
    
    if "k" in payload:  # kline/candlestick data
        kline = payload["k"]
        symbol = kline["s"]
        df = pd.DataFrame([{
            "symbol": symbol,
            "open_time": datetime.fromtimestamp(kline["t"] / 1000),
            "open": kline["o"],
            "high": kline["h"],
            "low": kline["l"],
            "close": kline["c"],
            "volume": kline["v"],
            "close_time": datetime.fromtimestamp(kline["T"] / 1000)
        }])
        print(df)
        insert_data(df, symbol)
        return df  

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def on_open(ws):
    params = [f"{symbol}@kline_1m" for symbol in SYMBOLS]  # 1m = 1 phút
    payload = {
        "method": "SUBSCRIBE",
        "params": params,
        "id": 1
    }
    ws.send(json.dumps(payload))

def start_ws():
    socket = "wss://stream.binance.com:9443/stream?streams=" + "/".join([f"{s}@kline_1m" for s in SYMBOLS])
    ws = websocket.WebSocketApp(
        socket,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open
    )
    ws.run_forever()
