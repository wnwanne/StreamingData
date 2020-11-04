import requests
import boto3
import uuid
import time
import random
import json


client = boto3.client('kinesis')
partition_key = str(uuid.uuid4())

x =True

while x:
    r = requests.get('https://randomuser.me/api/?exc=login').json()
    data = json.dumps(r)
    print(data)
    client.put_record(StreamName='', Data=data, PartitionKey=partition_key)
    time.sleep(random.uniform(0,1))
    # x = False