from lib.trader import Trader

class AvgTrader(Trader):
    def __init__ (self, init_asset) :
        super().__init__(init_asset)
        self.btc = 0.0
        self.position_list = []  # 매수할 때마다 기록

    def get_balance(self):
        return self.balance

    def get_btc(self):
        return self.btc

    def get_position_list(self):
        return self.position_list

    def buy(self, time, money, units, price):
        self.btc += units
        self.balance -= money

        # open position
        position = {
            'time': time,
            'units': units,
            'price': price,
            'total': money,
            'closed': False
        }
        self.position_list.append(position)

    def sell(self, btc, price, position):
        money = btc * price
        self.btc -= btc
        self.balance += money
        position.update(closed=True)

    def buy_or_sell(self, price_list):
        if len(price_list) < 20:
            return 'buy'

        price = 0
        for i in range(len(price_list) - 1):
            price += price_list[i]['price']

        price = price / 19
        if price > price_list[len(price_list) - 1]['price']:
            return 'buy'

        else:
            return 'sell'









