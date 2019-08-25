import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--age", help = "Happy Birthday, you are already X years old!", type=str)
args = parser.parse_args()
if args.age:
    print('Happy Birthday, you are already ' + args.age + ' years old!')