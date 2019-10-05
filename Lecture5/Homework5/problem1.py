def max(*args):
    a=0
    b=0
    for x in args:
        a+=1
        if a>0:
            if x>b:
                b=x
        else:
            b=x
    if a==0:
        print("no numbers given")
    else:
        print(b)
max(1,2,3,4,5,177,244)