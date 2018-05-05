import os
import time 

data = ['25/06/14', '22:12:36', 'Light Rain', '0', '65.1', '94', ['75.20', '63.90'], ['76.10', '60.60']]

def writeToCsv(datalist):
  header = ["date", "time", "weather", "uv", "Temp", "Pressure", "Humidity", "Magnetic Field", "\r"]

  fileName = str(time.strftime("%m_%d_%y_")+ "log.csv")
  if os.path.exists(fileName):
    f = open(fileName, "a")
  else:
    f = open(fileName, "a+")
    for element in header:
      f.write(element + ",")

  for element in datalist:
    if type(element)==str:
      f.write(element + ",")
    if type(element) == list:
      for i in element:
        f.write(i + ",")
  f.write("\r")
  f.close()
  print "Successfully printed to CSV"

writeToCsv(data)
