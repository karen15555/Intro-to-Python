def power(max):
    for x in range(max):
        yield 2**x
next(power(3))