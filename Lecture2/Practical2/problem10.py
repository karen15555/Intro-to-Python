import datetime
import time
import calendar


localtime = time.localtime()
print ("Local current time :", localtime)

tday = datetime.date.today()
print('Date: ', tday)
print('Year: ', tday.year)
print('Month: ', tday.month)
print('Week: ', tday.isoweekday())


