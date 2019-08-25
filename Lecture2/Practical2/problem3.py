import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name", help="Welcome, X!", type=str)
args = parser.parse_args()


print('Welcome, ' + args.name + "!")