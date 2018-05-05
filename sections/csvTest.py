import csv
import datetime

begin = datetime.datetime.now()
data = ['25/06/14', '22:12:36', 'Light Rain', '0', '65.1', '94', ['75.20', '63.90'], ['76.10', '60.60']]
dataList =[]
for element in data:
  if type(element)==str:
    dataList.append(element)
  if type(element) == list:
    for i in element:
      dataList.append(i)

print dataList

with open('csvFile.csv','a') as f:
    writer = csv.writer(f)
    writer.writerow([dataList[0]], dataList[1], dataList[2])
print datetime.datetime.now() - begin 