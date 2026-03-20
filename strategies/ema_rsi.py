from backtesting import Strategy
from backtesting.lib import crossover
from indicators.ema import ema
from indicators.rsi import rsi


class Ema_rsiStrategy(Strategy):
    # 默认参数（可被 Backtest.run(**params) 覆盖）
    ema_period = 20
    rsi_period = 14
    oversold = 30
    overbought = 70

    def init(self):
        # 注册指标（backtesting 推荐方式）
        self.ema = self.I(lambda x: ema(x, self.ema_period), self.data.Close)
        self.rsi = self.I(lambda x: rsi(x, self.rsi_period), self.data.Close)

    def next(self):
        price = self.data.Close[-1]

        # --- 开仓逻辑 ---
        # 价格向上突破 EMA + RSI 低位反弹 → 做多
        if crossover(self.data.Close, self.ema) and self.rsi[-1] < self.oversold:
            if not self.position:
                self.buy()

        # 价格向下跌破 EMA + RSI 高位 → 做空（或平多）
        elif crossover(self.ema, self.data.Close) and self.rsi[-1] > self.overbought:
            if self.position:
                self.position.close()