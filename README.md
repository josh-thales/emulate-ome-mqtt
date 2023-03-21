# emulate-ome-mqtt

Handles publishing to multiple MQTT topics with dynamic payloads at set intervals


  - [Prerequsities](#prerequsities)
  - [Set up](#set-up)
  - [Start publishing](#start-publishing)
    - [Creating payload functions](#creating-payload-functions)


## Prerequsities

`python`

## Set up
1. Clone repo
```
git clone https://github.com/josh-thales/emulate-ome-mqtt
```

2. Create `.env` file in root of folder with following contents (fill out appropriate fields):

```
HOST=
PORT=
USERNAME=
PASSWORD=
```

3. Install dependencies

```
pip install -r requirements.txt
```

## Start publishing

In `main.py` modify these variables to your preference:

1. `publishingData`
   - type: `list(tuple(str, function))`
     - where `str` is the topic and `function` is a function that returns the data to be published (python dict)
   - example: 
     ```py
     publishingData = [
         ("IW/Thales-1/NDATA/TEST", generateDataTest),
         ("IW/Thales-1/NDATA/TEST2", generateDataTest2),
     ]
     ```
2. `interval`
   - type: `int`
     - in seconds
   - example:
     ```py
     interval = 10
     ```

### Creating payload functions
To accuratley simulate the MQTT payloads, functions must be used as parameters, so timestamps values will be accurate with publishing times

For each topic you create you should create a new function that returns a py dict. When creating a timestamp, you should call the `zuluTime()` function

Here is an example function:
```py
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
```
