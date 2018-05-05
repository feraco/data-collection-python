# These modules are for system operations 
# like returning size of variables (size optimizations) or
# scanning the serial receive buffer.
import os
import sys 
import serial 
import time
import datetime

# Modules hit WUNDERGROUND API
# and introduce real-time weather data 
import urllib2
import json

# Log data to cloud with Xively 
import xively

# Global variables => I hate using them, but some functionality was easily implemented using them,
# so I gave in. 
global xively_success
global csv_success 
global wuLastUpdate
global wuData
global iterations
global geolookup

#Sets the initial sucess booleans to False
xively_success = False
csv_success = False

wuLastUpdate = datetime.datetime.strptime("", "")
wuData =[]

# Initial successful iteration count
iterations = 0

def getWunderground(geolookup):
  """ Geolookup = weather underground geolookup url: (http://www.wunderground.com/weather/api/d/docs?d=data/geolookup),
  determines if program has hit the API within the last 30 minutes. If yes, returns values of last API call.
  If no, it tries to call the API and returns a list of the current weather, current temp, rel humidity, and UV index.
  If there is no connection to the internet/ wunderground API, function returns a list with all values populated with "no connection".
  """
  dataFromWunderground = []
  global wuLastUpdate
  global wuData

  timeDelta = datetime.datetime.now()-wuLastUpdate
  print timeDelta
  if timeDelta >= datetime.timedelta(minutes=30):
    try:
      f = urllib2.urlopen(geolookup)
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
  return dataFromWunderground


def getDateTime():
  """Function grabs current time and date, then returns values in a 2-element list. """
  timeNow = time.strftime("%H:%M:%S")
  dateToday = time.strftime("%m/%d/%y")
  return [dateToday, timeNow]

def status(a, b):
  """ a = Xively success status. b = CSV success status."""
  if a and b:
        return "Xively and CSV updated"
  elif a:
    return "Xively updated but CSV not updated"
  elif b:
    return "CSV updated but Xively not updated"


def printXively(dataList):
  """datalist = list of weather underground data, current date and time, and sensor values. Function 
  iterates over the list, and writes each element to the proper Xively data stream."""
  global xively_success

  XIVELY_API_KEY = e456fc6a-5ab0-4697-b75f-6d3aebbeb782
  XIVELY_FEED_ID = 3eaac790-8a2c-4af6-9e49-9aaf8ffcc663
  api = xively.XivelyAPIClient(XIVELY_API_KEY)
  feed = api.feeds.get(XIVELY_FEED_ID)
  now = datetime.datetime.now()
  feed.datastreams = [
    xively.Datastream(id="uv", current_value=dataList[3], at=now),
    xively.Datastream(id="weather", current_value=dataList[2], at=now),
    xively.Datastream(id="exterior_temp", current_value=dataList[4], at=now),
    xively.Datastream(id="exterior_humidity", current_value=dataList[5], at=now),
    xively.Datastream(id="temp1", current_value=dataList[6][0], at=now),
    xively.Datastream(id="humidity1", current_value=dataList[6][1], at=now),
    xively.Datastream(id="temp2", current_value=dataList[7][0], at=now),
    xively.Datastream(id="humidity2", current_value=dataList[7][1], at=now),
    xively.Datastream(id="temp3", current_value=dataList[8][0], at=now),
    xively.Datastream(id="humidity3", current_value=dataList[8][1], at=now),
    xively.Datastream(id="temp4", current_value=dataList[9][0], at=now),
    xively.Datastream(id="humidity4", current_value=dataList[9][1], at=now),
    xively.Datastream(id="temp5", current_value=dataList[10][0], at=now),
    xively.Datastream(id="humidity5", current_value=dataList[10][1], at=now),
    xively.Datastream(id="temp6", current_value=dataList[11][0], at=now),
    xively.Datastream(id="humidity6", current_value=dataList[11][1], at=now),
    xively.Datastream(id="temp7", current_value=dataList[12][0], at=now),
    xively.Datastream(id="humidity7", current_value=dataList[12][1], at=now),

  ]

  feed.update()
  xively_success = True
  

def writeToCsv(datalist):
  """ function writes datalist values to a csv file. If daily csv file exists already, 
  list values are simply appended to end of file. If it does not, function creates the file, 
  then appends values. 
  """ 
  global csv_success

  header = ["date", "time", "weather", "uv", "Temp", "Pressure", "Humidity", "Magnetic Field", "\n"]

  fileName = str(time.strftime("%m_%d_%y_")+ "log.csv")
  if os.path.exists(fileName):
    f = open(fileName, "a")
  else:
    f = open(fileName, "a+")
    for element in header:
      f.write(element + ",")
    f.write("\n")

  for element in datalist:
    if type(element)==str:
      f.write(element + ",")
    if type(element) == list:
      for i in element:
        f.write(i + ",")
  f.write("\n")
  f.close()
  csv_success = True


def mainLoop():
  """mainLoop checks the serial receive buffer for activity. If it sees anything, it grabs 
  current date/time and weather underground data. It grabs the semi-colon/colon separated values in the 
  serial buffer, appends them to the array already containing date/time/wunderground data, and tries to 
  write array to a CSV and Xively. It then increases the iteration count by 1, and puts the program to sleep
  for 4.5 minutes (to save resources on host computer). The arduino sends data every 5 minutes, so a 4.5 minute
  sleep cycle is plenty long enough to conserve resouces without mistiming data transfer. """ 

  global xively_success
  global csv_success
  global iterations
  global geolookup

  data = []
  ser = serial.Serial("/dev/tty.usbmodem1421", 115200)
  print "Serial Initialized"

  while 1:
    if ser.inWaiting():
      datetimeData = getDateTime()
      weatherData = getWunderground()

      for i in datetimeData:
        data.append(i)
      for i in weatherData:
        data.append(i)
      val = ser.readline().strip('\n\r').split(';')
      
      for i in range(0, len(val)):
        sensorData = val[i].split(':')
        data.append(sensorData)

      data.append(str(iterations))

      try: 
        writeToCsv(data)
        csv_success = True
      except:
        csv_success = False
      try:
        printXively(data)
        xively_success = True
      except:
        try:
          printXively(data)
          xively_success = True
        except:
          xively_success = False

      print status(xively_success, csv_success), ": ", data 
      iterations += 1
      data = []

      time.sleep(270)

mainLoop()
