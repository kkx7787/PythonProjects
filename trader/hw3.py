import sys
from lib.bitstamp_info import *
from lib.trader import Trader
from lib.currency_info import *

BUY_PERCENT = 0.03
SELL_PERCENT = 1.03
INIT_ASSET = 1000000


if __name__ == '__main__':

    trader = Trader(INIT_ASSET) # Trader 클래스로 시작
    krw_usd = get_currency()  # TODO: beautifulsoup을 이용해 환율 정보 가져와서 대입하기
    for price_info in get_price_list('1d'):
        current_time = price_info['time']
        current_price = price_info['price'] * float(krw_usd)

        # BUY
        if True:
            buy_amount = trader.get_balance() * BUY_PERCENT # 1000 * 일정부분

            if trader.get_balance() > buy_amount:
                units = buy_amount / current_price
                trader.buy(current_time, buy_amount, units, current_price)

        # SELL
        if True:
            for p in trader.get_position_list():
                if not p['closed']:
                    buy_price = p['price']
                    units = p['units']
                    if current_price > buy_price * SELL_PERCENT:
                        trader.sell(units, current_price, p)

        calculated_asset = trader.get_btc() * current_price + trader.get_balance()

        # date asset available_asset btc price
        sys.stdout = open('hw3.txt', 'a')
        print(current_time + ' {0:7d}'.format(int(calculated_asset)) + ' {0:7d}'.format(int(calculated_asset)) + ' {0:1.5f}'.format(trader.get_btc()) + ' {0:7d}'.format(int(current_price)))
