from pprint import pprint
import boto3
from tiingo import TiingoClient
from settings import (
    AWS_ACCESS_KEY,
    AWS_SECRET_KEY,
)


sns_client = boto3.client(
    "sns",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name="us-east-1",
)

tiingo_client = TiingoClient()
ticker_price = tiingo_client.get_ticker_price("DIA", frequency="1Min")[-1]


topic_arn = sns_client.list_topics().get("Topics")[0].get("TopicArn")

message = "DIA closing price {} @ {}".format(
    ticker_price["close"], ticker_price["date"]
)

response = sns_client.publish(TopicArn=topic_arn, Message=message, Subject="Dow Daily",)
print(response)
