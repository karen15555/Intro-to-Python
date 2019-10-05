l1=['a',0,2]
print(l1)
for x in l1:
    print("x:", x)
    try:
        a=x**(-1)
        print('The reciprocal of', x, 'is', a)
    except Exception:
        print('Oops!')