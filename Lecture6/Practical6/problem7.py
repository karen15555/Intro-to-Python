def sum(x,y):
    assert (isinstance(x, int) and isinstance(y, int)), 'Arguments of type int required'
    return x+y

d=sum(10,15)
print(d)

c=sum(10,'hello')
print(c)