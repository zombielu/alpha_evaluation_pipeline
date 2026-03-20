from backtesting import Strategy
from indicators.rsi import rsi

class RsiStrategy(Strategy):
    period = 14
    oversold = 30
    overbought = 70

    def init(self):
        self.rsi = self.I(lambda x: rsi(x, self.period), self.data.Close)

    def next(self):
        if self.rsi[-1] < self.oversold:
            self.buy(size=0.95)
        elif self.rsi[-1] > self.overbought:
            self.sell()