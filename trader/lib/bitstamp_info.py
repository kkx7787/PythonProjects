import ccxt
from datetime import datetime


def get_current_price():
    bitstamp = ccxt.bitstamp()
    ticker = bitstamp.fetch_ticker('BTCUSD')
    return float(ticker['close'])


def get_price_list(time_frame):
    try:
        bitstamp = ccxt.bitstamp()
        price_list = []

        if bitstamp.has['fetchTicker']:
            ohlcvs = bitstamp.fetch_ohlcv('BTC/USD', time_frame)

            for ohlcv in ohlcvs:
                s = datetime.fromtimestamp(ohlcv[0] / 1000).strftime('%Y-%m-%d')  # 날짜
                o = ohlcv[1]
                h = ohlcv[2]
                l = ohlcv[3]
                c = ohlcv[4]  # 가격
                d = {'time': s, 'price': c}
                price_list.append(d)
        return price_list
    # [{'2022-11-29', '11359'}]

    except Exception as ex:
        print(ex)
        return None
