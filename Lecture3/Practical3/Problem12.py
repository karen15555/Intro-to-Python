import argparse

pars=argparse.ArgumentParser()

pars.add_argument("set1",type=int)
args=pars.parse_args()

set3 = {1, 3, 5, 2, 34}

list1=list(set3)

b=min(list1)
c=max(list1)
a=args.set1

if(a>b and a<c):
    print(True)
else:
    print(False)