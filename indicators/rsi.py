import numpy as np

def rsi(close, period=14):

    close = np.asarray(close)
    delta = np.diff(close, prepend=close[0])

    gain = np.maximum(delta, 0)
    loss = np.maximum(-delta, 0)

    avg_gain = np.zeros_like(close)
    avg_loss = np.zeros_like(close)

    avg_gain[period] = gain[:period].mean()
    avg_loss[period] = loss[:period].mean()

    for i in range(period + 1, len(close)):
        avg_gain[i] = (avg_gain[i-1]*(period-1) + gain[i]) / period
        avg_loss[i] = (avg_loss[i-1]*(period-1) + loss[i]) / period

    rs = avg_gain / (avg_loss + 1e-10)
    rsi = 100 - (100 / (1 + rs))

    return rsi