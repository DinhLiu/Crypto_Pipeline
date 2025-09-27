import psycopg2
from psycopg2.extras import execute_values
from config import DB_CONFIG

def create_table():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS crypto_prices (
        id SERIAL PRIMARY KEY,
        symbol TEXT,
        open_time TIMESTAMP,
        open NUMERIC,
        high NUMERIC,
        low NUMERIC,
        close NUMERIC,
        volume NUMERIC
    )
    """
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()


def insert_data(df):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    query = """
    INSERT INTO crypto_prices (symbol, open_time, open, high, low, close, volume)
    VALUES %s
    """

    values = [
        (
            row.symbol,
            row.open_time,
            float(row.open),
            float(row.high),
            float(row.low),
            float(row.close),
            float(row.volume)
        )
        for row in df.itertuples(index=False)
    ]

    execute_values(cur, query, values)
    conn.commit()
    cur.close()
    conn.close()
