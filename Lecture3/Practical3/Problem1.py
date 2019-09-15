import sys

list1 = ["hello", 1, True]
print(list1)

#sys.argv[0] means Problem1.py, hence we start from [1:]

new_list1 = (sys.argv[1:])
print(list1+new_list1)



