import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", help="string type mandatory argument",type=str)
args = parser.parse_args()

usacount=args.text.lower().count("usa")

print("The given string:", args.text)
print("The USA count is:", usacount)
print("The new string:",args.text.lower().replace("USA","Armenia").replace("usa","Armenia"))