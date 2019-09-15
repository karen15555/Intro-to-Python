list5 = ['Berlin', 'hello', 555, 'Deutsche Bank', 60325, 15555]
print('List before del:', list5)
list6=list5.copy()
# if you want to del 0,4,5 start from the end
del list6[-6]
del list6[-2]
del list6[-1]
#list5.pop(0), list5.pop(4), list5.pop(5)
print('List after del:', list6)