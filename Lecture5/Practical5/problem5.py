def grade(name, *arg):
    a=0
    b=0
    for x in arg:
        a+=x
        b+=1
    if b==0:
        a=0
    else:    
        a/=b    
    print(name+",","your average grade is",a)
grade("Karen",1,2,3,1,1,1,1,3.3)
