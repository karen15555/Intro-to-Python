import argparse

parser = argparse.ArgumentParser()

parser.add_argument("s1", help="A sAmpLe stRING", type=str)

args = parser.parse_args()

print(args.s1.upper())
print(args.s1.lower())



