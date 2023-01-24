class Trader:
    def __init__(self, init_asset):
        self.balance = init_asset
        self.btc = 0.0
        self.position_list = [] # 매수할 때마다 기록

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
