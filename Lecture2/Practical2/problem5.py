import argparse

parser = argparse.ArgumentParser()

parser.add_argument("s1", help="A sAmpLe stRING", type=str)

args = parser.parse_args()

print(“All uppercase: " + args.s1.upper())
print(“All lowercase: " + args.s1.lower())



