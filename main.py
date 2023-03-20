from datetime import datetime, timezone
from mqttInterface import startPublishing


def zuluTime():
    return str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))


def generateDataTest():
    return {
        "TagType": "BoolTag",
        "Name": "TEST",
        "DataType": "Bool",
        "IOType": "InOut",
        "Units": "",
        "PublishedTimeStamp": zuluTime(),
        "Readings": [{"TimeStamp": zuluTime(), "Value": True, "Quality": 1}],
    }


publishingData = [
    ("IW/Thales-1/NDATA/TEST", generateDataTest),
    ("IW/Thales-1/NDATA/TEST2", generateDataTest),
]
interval = 10

startPublishing(publishingData, interval)
