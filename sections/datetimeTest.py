import datetime
import time 


def getDateTime():
  timeNow = time.strftime("%H:%M:%S")
  dateToday = time.strftime("%d/%m/%y")
  print [dateToday, timeNow]


print str(getDateTime())