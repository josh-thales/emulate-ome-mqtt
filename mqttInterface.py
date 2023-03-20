import json
import time
from dotenv import dotenv_values
import paho.mqtt.publish as publish

config = {
    **dotenv_values(".env"),
}

def pub(topic, data):
    publish.single(
        topic=topic,
        payload=json.dumps(data),
        hostname=config["HOST"],
        port=int(config["PORT"]),
        auth={"username": config["USERNAME"], "password": config["PASSWORD"]},
        tls={},
    )

def startPublishing(publishingData, interval):
    while True:
        for publishData in publishingData:
            pub(publishData[0], publishData[1]())

        time.sleep(interval)

