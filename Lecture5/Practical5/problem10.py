def list_els(list1):
    for x in list1:
        yield x

l1=[2,3,4,5,6,7,8,9,10]
print(next(list_els(l1)))