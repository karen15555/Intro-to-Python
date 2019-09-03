import argparse

parser = argparse.ArgumentParser()

parser.add_argument("script", help = "script", type=str)
parser.add_argument("int1", help = "integer 1", type=int)
parser.add_argument("int2", help = "integer 2", type=int)
args = parser.parse_args()

print("The given text: "+args.script)
print("Start index:",args.int1)
print("End index:",args.int2)
print("Output string: ")

print(args.script[args.int1::args.int2])