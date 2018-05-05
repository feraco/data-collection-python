import xively
import datetime
import time 

data = ['25/06/14', '22:12:36', 'Light Rain', '0', '65.1', '94', ['75.20', '63.90'], ['76.10', '60.60']]

XIVELY_API_KEY = 'e456fc6a-5ab0-4697-b75f-6d3aebbeb782'
XIVELY_FEED_ID = 3eaac790-8a2c-4af6-9e49-9aaf8ffcc663

api = xively.XivelyAPIClient(XIVELY_API_KEY)
feed = api.feeds.get(XIVELY_FEED_ID)

for i in range(0,10):
  now = str(datetime.datetime.now())
  feed.datastreams = [
    xively.Datastream(id="uv", current_value=data[3], at=now)
    xively.Datastream(id="weather", current_value=data[2], at=now)
    xively.Datastream(id="exterior_temp", current_value=data[4], at=now),
    xively.Datastream(id="exterior_humidity", current_value=data[5], at=now),
    xively.Datastream(id="temp1", current_value=data[6][0], at=now),
    xively.Datastream(id="humidity1", current_value=data[6][1], at=now)
  ]

  feed.update()
  print "update" + str(i+1)

