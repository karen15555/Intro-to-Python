def average(x,y,z):
    avg = (x+y+z)/3
    return avg
average(3,10,15)

print ("calculate an average of first n natural numbers")
n = input("Enter Number")
n = int (n)
average = 0
sum = 0
for num in range(0,n+1,1):
    sum = sum+num;
average = sum / n
print("Average of first ", n, "number is: ", average)

sum = 0
list = [1,2,3,4,5,6,7]
for num in list:
    sum = sum +num
average  = sum / len(list)
print ("sum of list element is : ", sum)
print ("Average of list element is ", average )