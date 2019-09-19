x = int(input())
y = int(input())

if x > y:
    print("The number " + str(x) + " is the greatest")
else:
    print("The number " + str(y) + " is the greatest")


maxnumber = int(max(x,y))
print(maxnumber)

print("The number " + str(maxnumber) + " is the greatest")