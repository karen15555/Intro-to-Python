list1=['al', 'abc', 'xyz', 'as', 'aba','1221']

a = 0
b = 0

for c in list1:
    if len(c)>1:
        a+=1
    if c[0]==c[-1]:
        b+=1
        
print(a)
print(b)