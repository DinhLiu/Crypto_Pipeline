import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import mplfinance as mpf
from config import DB_CONFIG

# Kết nối DB
conn = psycopg2.connect(**DB_CONFIG)

# Tạo figure với 2 axes: giá + volume
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(2,1,1)   # trục giá
ax2 = fig.add_subplot(2,1,2, sharex=ax)  # trục volume

my_style = mpf.make_mpf_style(
    base_mpf_style='charles',
    gridstyle='--',
    gridaxis='both',
)

def get_data():
    query = "SELECT * FROM crypto_btcusdt ORDER BY open_time DESC LIMIT 50"
    df = pd.read_sql(query, conn)
    df['open_time'] = pd.to_datetime(df['open_time'])
    df[['open','high','low','close','volume']] = df[['open','high','low','close','volume']].astype(float)
    df = df.sort_values("open_time").set_index("open_time")
    return df

def animate(i):
    df = get_data()
    ax.clear()
    ax2.clear()

    mpf.plot(
        df,
        type='candle',
        style=my_style,
        ax=ax,
        volume=ax2,
        ylabel="Price (USDT)",
        ylabel_lower="Volume",
        xrotation=15,
        show_nontrading=True
    )
    # Bật grid ngang + dọc (ô vuông)
    ax.set_axisbelow(True)
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    ax2.set_axisbelow(True)
    ax2.grid(True, which='both', linestyle='--', alpha=0.5)

ani = FuncAnimation(fig, animate, interval=60000)  # update mỗi 60 giây
plt.show()
