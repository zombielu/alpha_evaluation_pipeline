import pandas as pd

def ema(series, period: int):
    series = pd.Series(series)

    return series.ewm(span=period, adjust=False).mean().values