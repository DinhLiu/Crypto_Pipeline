import psycopg2
from psycopg2.extras import execute_values
from config import DB_CONFIG

def insert_data(df, symbol):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    table_name = f"crypto_{symbol.lower()}"
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            open_time TIMESTAMP,
            open NUMERIC,
            high NUMERIC,
            low NUMERIC,
            close NUMERIC,
            volume NUMERIC,
            close_time TIMESTAMP
        )
    """)

    values = [
        (
            row.open_time.to_pydatetime(),
            row.open,
            row.high,
            row.low,
            row.close,
            row.volume,
            row.close_time.to_pydatetime()
        )
        for row in df.itertuples(index=False)
    ]

    query = f"INSERT INTO {table_name} (open_time, open, high, low, close, volume, close_time) VALUES %s"
    execute_values(cur, query, values)

    conn.commit()
    cur.close()
    conn.close()
