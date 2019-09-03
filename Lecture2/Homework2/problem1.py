import argparse
import datetime
import time

parser = argparse.ArgumentParser()
parser.add_argument("--year", help="year",type=int)
parser.add_argument("--day", help="day",type=int)
args = parser.parse_args()

now=datetime.datetime.now()
print(now)

if(args.year!=None):
    td1=datetime.timedelta(days=args.year*365)
    print("Given years:",args.year)
    now+=td1
else:
    print("Given years: not given")

if(args.day!=None):
    td1=datetime.timedelta(days=args.day) 
    print("Given days:",args.day)
    now+=td1
  
else:
    print("Given days: not given")


print("Final date:",now)
