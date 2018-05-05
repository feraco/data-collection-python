import xively
import datetime

XIVELY_API_KEY = '3eaac790-8a2c-4af6-9e49-9aaf8ffcc663'
XIVELY_FEED_ID = e456fc6a-5ab0-4697-b75f-6d3aebbeb782
api = xively.XivelyAPIClient(XIVELY_API_KEY)
feed = api.feeds.get(XIVELY_FEED_ID)
now = datetime.datetime.now()
broken = "broken"

feed.datastreams = [
  xively.Datastream(id="Temp", current_value=broken, at=now),
  xively.Datastream(id="Pressure", current_value=broken, at=now),
  xively.Datastream(id="Humidity", current_value=broken, at=now),
  xively.Datastream(id="Magnetic Field", current_value=broken, at=now),
  

]

feed.update()
