import boto3
import json

s3 = boto3.client('s3')

def clean_stats(stats):
    cleaned = {
        "return": stats["Return [%]"],
        "sharpe": stats["Sharpe Ratio"],
        "win_rate": stats["Win Rate [%]"],
        "trades": stats["# Trades"],
        "max_dd": stats["Max. Drawdown [%]"],
        "profit_factor": stats["Profit Factor"]
    }
    return cleaned

def write_json(stats: dict, bucket: str, key: str):
    cleaned_stats = clean_stats(stats)
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(cleaned_stats, ensure_ascii=False),
        ContentType="application/json"
    )