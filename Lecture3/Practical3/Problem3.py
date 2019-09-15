import argparse
new_list2 = ['Berlin', 'hello', 555, 'Deutsche Bank', 60325, 555]

parser = argparse.ArgumentParser()

parser.add_argument("list2", type=int)
args = parser.parse_args()

ptint(new_list2)
count = list2.count(new_list2)
print('Number of', args.list2,"=", new_list2.count(args.list2))

