def is_even_num(l):
    evennum=[]
    for n in l:
        if n%2==0:
            evennum.append(n)
    return evennum
print(len(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))) 



num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even number".format(num))
else:
    print("{0} is Odd number".format(num))  