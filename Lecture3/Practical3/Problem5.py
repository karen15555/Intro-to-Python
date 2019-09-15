list5 = ['Berlin', 'hello', 555, 'Deutsche Bank', 60325, 15555]
print('List before del:', list5)
# if you want to del 0,4,5 start from the end
del list5[-6]
del list5[-2]
del list5[-1]
#list5.pop(0), list5.pop(4), list5.pop(5)
print('List after del:', list5)
