# TradingView Technical Analysis API

A simple Flask API that provides technical analysis data using TradingView indicators.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the Flask application:

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## Endpoints

#### GET /analyze

Analyze a trading pair using TradingView indicators.

Query Parameters:
- `symbol` (optional): Trading pair symbol (default: BTCUSDT)
- `interval` (optional): Time interval (default: 1h)

Supported intervals:
- 1m (1 minute)
- 5m (5 minutes)
- 15m (15 minutes)
- 1h (1 hour)
- 4h (4 hours)
- 1d (1 day)
- 1W (1 week)
- 1M (1 month)

Example request:
```
GET http://localhost:5000/analyze?symbol=ETHUSDT&interval=4h
```

The response will include:
- Summary recommendation
- Buy/Sell signals
- Oscillator metrics
- Moving average metrics
- Technical indicators

#### GET /rsi

Get real-time RSI (Relative Strength Index) values for a trading pair.

Query Parameters:
- `symbol` (optional): Trading pair symbol (default: BTCUSDT)
- `interval` (optional): Time interval (default: 1h)

Example request:
```
GET http://localhost:5000/rsi?symbol=ETHUSDT&interval=4h
```

The response will include:
- RSI value
- RSI status (BUY/SELL/NEUTRAL)
- Timestamp of the analysis
- Symbol and interval information


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
