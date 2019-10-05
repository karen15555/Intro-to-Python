def div(x,y):
    try:
        return x/y
    except Exception:
        print('Sorry, this number is zero')

d=div(15,10)
print(d)

c=div(10,0)
print(c)