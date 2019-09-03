import datetime
import time
import calendar

bday=datetime.date(1986, 1, 14)
print(bday)
print(bday.year)
print(bday.month)
print(bday.day)
print(bday.isoweekday())

newbday=datetime.date(2020,1,14)
tday=datetime.datetime.today()
print(newbday-tday)

cal = calendar.month(2017, 5)
print(cal)

tdelta = datetime.timedelta(days = 1)
ytday = tday-tdelta
print(ytday)

ytday+=2*tdelta
print(ytday)

ytday-=3*tdelta
print(ytday)
