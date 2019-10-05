def unique(l1):
    res=[]
    for i in l1:
        if l1.count(i)==1:
            res.append(i)
    return res

l1=[2,4,8,8,12,12,12,16,18,20,20,20]


print(unique(l1))