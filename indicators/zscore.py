import pandas as pd

def zscore(series: pd.Series, window: int = 20) -> pd.Series:
    return (series - series.rolling(window).mean()) / series.rolling(window).std()