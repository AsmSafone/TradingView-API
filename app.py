from flask_cors import CORS
from src import TA_Handler, Interval
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/')
def index():
    return jsonify(
        {'name': 'TradingView Technical Analysis API',
         'version': '1.0.0',
         'description': 'Analyze technical indicators for a given symbol and interval.',
         'author': 'Safone',
         'license': 'MIT'
         }
    )


@app.route('/analyze', methods=['GET'])
def analyze():
    symbol = request.args.get('symbol', 'BTCUSDT')
    interval = request.args.get('interval', '1h')
    
    # Convert interval string to tradingview_ta Interval
    interval_map = {
        '1m': Interval.INTERVAL_1_MINUTE,
        '5m': Interval.INTERVAL_5_MINUTES,
        '15m': Interval.INTERVAL_15_MINUTES,
        '1h': Interval.INTERVAL_1_HOUR,
        '4h': Interval.INTERVAL_4_HOURS,
        '1d': Interval.INTERVAL_1_DAY,
        '1W': Interval.INTERVAL_1_WEEK,
        '1M': Interval.INTERVAL_1_MONTH
    }
    
    tv_interval = interval_map.get(interval, Interval.INTERVAL_1_HOUR)
    
    try:
        handler = TA_Handler(
            symbol=symbol,
            screener="crypto",
            exchange="BINANCE",
            interval=tv_interval
        )
        analysis = handler.get_analysis()
        
        return jsonify({
            'symbol': symbol,
            'interval': interval,
            'summary': {
                'recommendation': analysis.summary['RECOMMENDATION'],
                'buy_signals': analysis.summary['BUY'],
                'sell_signals': analysis.summary['SELL'],
                'neutral_signals': analysis.summary['NEUTRAL']
            },
            'oscillators': analysis.oscillators,
            'moving_averages': analysis.moving_averages,
            'indicators': analysis.indicators
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/rsi', methods=['GET'])
def get_rsi():
    symbol = request.args.get('symbol', 'BTCUSDT')
    interval = request.args.get('interval', '1h')
    
    # Convert interval string to tradingview_ta Interval
    interval_map = {
        '1m': Interval.INTERVAL_1_MINUTE,
        '5m': Interval.INTERVAL_5_MINUTES,
        '15m': Interval.INTERVAL_15_MINUTES,
        '1h': Interval.INTERVAL_1_HOUR,
        '4h': Interval.INTERVAL_4_HOURS,
        '1d': Interval.INTERVAL_1_DAY,
        '1W': Interval.INTERVAL_1_WEEK,
        '1M': Interval.INTERVAL_1_MONTH
    }
    
    tv_interval = interval_map.get(interval, Interval.INTERVAL_1_HOUR)
    
    try:
        handler = TA_Handler(
            symbol=symbol,
            screener="crypto",
            exchange="BINANCE",
            interval=tv_interval
        )
        analysis = handler.get_analysis()
        
        return jsonify({
            'symbol': symbol,
            'interval': interval,
            'rsi': analysis.indicators['RSI'],
            'rsi_status': analysis.oscillators['COMPUTE']['RSI'],
            'timestamp': analysis.time
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
