# Crypto Pipeline

## Project Overview

This repository provides a cryptocurrency data pipeline with two main modules:

- `UsingRestAPI/`: Fetches and loads cryptocurrency data from Binance using REST API.
- `UsingWebSocket/`: Fetches and loads real-time cryptocurrency data from Binance using WebSocket.

The project is designed to collect data for multiple symbols (BTCUSDT, ETHUSDT, BNBUSDT, ADAUSDT, SOLUSDT) and store it in a database. Configuration (API keys, DB credentials) is managed via environment variables loaded from a `.env` file.

## Directory Structure

```
config.py
UsingRestAPI/
    api_main.py
    fetch_data.py
    load_data.py
UsingWebSocket/
    ws_main.py
    ws_client.py
    load_data.py
```

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/DinhLiu/Crypto_Pipeline.git
cd Crypto_Pipeline
```

### 2. Create a Virtual Environment (Recommended)

```sh
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Required Packages

Install the following Python packages:

```sh
pip install python-dotenv requests websockets
```

Depending on your database (e.g., PostgreSQL, MySQL), you may also need:

- For PostgreSQL: `psycopg2-binary`
- For MySQL: `mysql-connector-python`

Example for PostgreSQL:

```sh
pip install psycopg2-binary
```

### 4. Environment Variables

Create a `.env` file in the root directory with the following content:

```
BINANCE_API_KEY=your_binance_api_key
BINANCE_API_SECRET=your_binance_api_secret
DB_HOST=your_db_host
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_PORT=your_db_port
```

For `your_binance_api_key` and `your_binance_api_secret`, you can get it at [Binance](https://www.binance.com/en/binance-api)

### 5. Running the Project

- To fetch data using REST API:
  ```sh
  python UsingRestAPI/api_main.py
  ```
- To fetch data using WebSocket:
  ```sh
  python UsingWebSocket/ws_main.py
  ```

## Additional Notes

- Ensure that your database is running and accessible from the machine where you are running this pipeline.
- For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/DinhLiu/Crypto_Pipeline/issues).
- Consider reviewing the code and contributing if you have suggestions for improvements or additional features.