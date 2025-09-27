from UsingRestAPI.fetch_data import get_price
from UsingRestAPI.load_data import create_table, insert_data

def main():
    print("Fetching data from Binance...")
    df = get_price(interval="5m", limit=50)
    print("Success")

    print("Creating table (if not exists)...")
    create_table()
    print("Success")

    print("Inserting data into PostgreSQL...")
    insert_data(df)
    print("Success")
    
    print("Data saved to database successfully.")

if __name__ == "__main__":
    main()
