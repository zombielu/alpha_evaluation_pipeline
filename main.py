import importlib
import boto3
import pandas as pd
import yaml
from backtesting import Backtest
from engine import loader, writer



# S3 设置
BUCKET = "quant-platform"
DATA_KEY = "raw/OANDA_XAUUSD, 15_c1cf9.csv"
s3 = boto3.client('s3')


if __name__ == '__main__':
    # load data
    df = loader.load_csv(BUCKET, DATA_KEY)


    # 读取策略配置
    with open("config/strategies.yml") as f:
        config = yaml.safe_load(f)

    for strat in config['strategies']:
        name = strat['name']
        params = strat.get('params', {})

        # 动态导入策略类
        module = importlib.import_module(f"strategies.{name}")
        StrategyClass = getattr(module,
                                f"{name.capitalize()}Strategy")  # e.g., EMAStrategy

        bt = Backtest(df.copy(), StrategyClass, cash=100000, commission=0, trade_on_close=True, finalize_trades=True)
        stats = bt.run(**params)
        print(f"{name} stats:\n", stats)

        # 保存 summary stats JSON
        writer.write_json(stats, bucket=BUCKET, key=f"results/{name}_stats.json")



