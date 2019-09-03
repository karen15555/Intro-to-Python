import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str", help="string type text",type=str)
parser.add_argument("word1", help="word #1",type=str)
parser.add_argument("word2", help="word #2",type=str)
args = parser.parse_args()

print("The given text:", args.str)
print("First word:", args.word1)
print("Second word:", args.word2)
print("Output string:",args.str.replace(args.word1,args.word2))
