from datetime import datetime, timezone
from mqttInterface import startPublishing
from omes import omes


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


publishingData = [*omes]
interval = 60


print("\nStarting Emulation for topics:")
for publishData in publishingData:
    print(f"\t- {publishData[0]}")
print(f"Every {interval} seconds\n")

startPublishing(publishingData, interval)
