import pandas as pd
import boto3

s3 = boto3.client('s3')

def load_csv(bucket: str, key: str) -> pd.DataFrame:
    resp = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(
        resp['Body'],
        usecols=['open', 'high', 'low', 'close', 'time']
    )
    df = df.rename(columns={
        'open': 'Open',
        'high': 'High',
        'low': 'Low',
        'close': 'Close'
    })
    return df