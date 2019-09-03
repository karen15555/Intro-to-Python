import datetime
import time
import calendar


localtime = time.localtime()
print ("Local current time :", localtime)
tnow = datetime.datetime.now().time()
print(tnow)

tday = datetime.date.today()
print('Date: ', tday)
print('Year: ', tday.year)
print('Month: ', tday.month)
print('Week: ', tday.isoweekday())

tday = datetime.date.today()
print('Date today: ', tday)
tdelta1 = datetime.timedelta(days = 5)
print(tdelta1)
print('Date today - 5 days: ', tday - tdelta1)

tdelta2 = datetime.timedelta(seconds = 5)
print(tdelta2)

print('Time now + 5 seconds: ', tnow + tdelta2)