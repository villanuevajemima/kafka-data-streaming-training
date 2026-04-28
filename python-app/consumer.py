from confluent_kafka import Consumer
from pymongo import MongoClient
import json

# Setup
conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "de-training-group",
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(conf)
consumer.subscribe(['training_topic'])

mongo_client = MongoClient("mongodb://localhost:27017")
db = mongo_client.training_db

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None: continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        data = json.loads(msg.value().decode('utf-8'))
        db.raw_events.insert_one(data)
        print(f"Saved to Mongo: {data}")
finally:
    consumer.close()