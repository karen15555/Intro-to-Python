import argparse
parser = argparse.ArgumentParser()

parser.add_argument("set1", type=int)
args = parser.parse_args()

set2 = {1, 3, 5, 2, 34}
print(set2)
if args.set1 in set2:
    set2.remove(args.set1)
print(set2)