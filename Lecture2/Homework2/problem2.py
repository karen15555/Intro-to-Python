import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str", help="7 and more odd length",type=str)
args = parser.parse_args()

a = len(args.str)
a-=1
a/=2
a=int(a)

print("The given text:", args.str)
mid = args.str[(a-1):(a+2)]
print("Middle 3 characters:", mid)
print("The new string:",args.str[:(a-1)]+mid.upper()+args.str[a+2:])