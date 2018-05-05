import datetime
import time

import urllib2
import json
global wuLastUpdate
global wuData

wuLastUpdate = datetime.datetime.strptime("", "")
wuData = []

## What do we want to get from WUNDERGROUND? 
## Relative Humidity
## Temp_f
## Weather 

def getWunderground():
  dataFromWunderground = []
  global wuLastUpdate
  global wuData

  timeDelta = datetime.datetime.now()-wuLastUpdate
  print timeDelta
  if timeDelta >= datetime.timedelta(minutes=30):
    #dataFromWunderground = []
    try:
      f = urllib2.urlopen('http://api.wunderground.com/api/11a21736da16cda4/geolookup/conditions/q/NY/Huntington.json')
      json_string = f.read()
      parsed_json = json.loads(json_string)
      weather = parsed_json["current_observation"]["weather"]
      temp_f = parsed_json["current_observation"]["temp_f"]
      relative_humidity = parsed_json["current_observation"]["relative_humidity"]
      uv = parsed_json["current_observation"]["UV"]
      #pressure_in = parsed_json["current_observation"]["pressure_in"]
      #wind_degrees = parsed_json["current_observation"]["wind_degrees"]
      #wind_mph = parsed_json["current_observation"]["wind_mph"]
      f.close()
      dataFromWunderground = [str(weather), str(uv), str(temp_f), str(relative_humidity[:-1]) ]
      wuData = dataFromWunderground
      wuLastUpdate = datetime.datetime.now()
    except:
      for i in range(0,4):
        dataFromWunderground.append("No connection")
      wuData = dataFromWunderground
      wuLastUpdate = datetime.datetime.now()
  else:
    dataFromWunderground = wuData
  print dataFromWunderground
  print wuLastUpdate, datetime.datetime.now()

getWunderground()
