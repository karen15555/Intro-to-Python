import argparse

parser=argparse.ArgumentParser()

parser.add_argument("set1",help="set1",type=str)
parser.add_argument("set2",help="set2",type=str)

args=parser.parse_args()

dict1={'key1':'Frankfurt','key2':'Deutschland'}
print(dict1)

dict1[args.set1]=args.set2
print(dict1)