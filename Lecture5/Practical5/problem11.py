def iter_num(n):
    for x in range(1,(n+1)):
        yield x
next(iter_num(11))