def my_range(n):
    for x in range(n+2):
        if x==n+1:
            print("There are no values left.")
        else:
            yield x

a=my_range(15)
for x in range(17):
    print(next(a))