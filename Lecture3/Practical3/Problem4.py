import argparse
parser = argparse.ArgumentParser()

parser.add_argument("list4", type=int)
args = parser.parse_args()
new_list4 = ['Berlin', 'hello', 555, 'Deutsche Bank', 60325, 15555]
print('List before del:',new_list4)
del new_list4[0]
print('List after del:',new_list4)

