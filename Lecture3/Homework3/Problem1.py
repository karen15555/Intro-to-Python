a=[1,4,5,7,8,-2,0,-1]
a_sorted=list()
print(a[2],a[4])

a_sorted=a.copy()
a_sorted.sort()
a_sorted.reverse()
print(a_sorted[1::4])
print(a_sorted[2::7])

a_sorted.pop(2)
a_sorted.pop(2)
print(a_sorted)


b=["grapes","Potatoes","tomatoes","Orange","Lemon","Broccoli","Carrot","Sausages"]
b_sorted=b.copy()
b_sorted.sort()


c=[]
c.extend(a[1:4])
c.extend(b[4:7])
print(c)