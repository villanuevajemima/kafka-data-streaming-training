from confluent_kafka import Producer
import json
import time

conf = {'bootstrap.servers': "localhost:9092"}
producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

while True:
    data = {"sensor_id": 1, "value": 23.5, "unit": "celsius"}
    producer.produce('training_topic', json.dumps(data).encode('utf-8'), callback=delivery_report)
    producer.flush()
    time.sleep(5)