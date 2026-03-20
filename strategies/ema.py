from backtesting import Strategy
from backtesting.lib import crossover
from indicators.ema import ema
import pandas as pd

class EmaStrategy(Strategy):
    period = 20  # 默认参数，可以在 Backtest 时 override

    def init(self):
        # 初始化指标，self.data.Close 是 backtesting 框架里的价格序列
        self.ema = self.I(lambda x: ema(x, self.period), self.data.Close)

    def next(self):
        if crossover(self.data.Close, self.ema):
            self.buy(size=0.95)
        elif crossover(self.ema, self.data.Close):
            self.sell()