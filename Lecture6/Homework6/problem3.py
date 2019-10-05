import time 
def dec(func):
    def wrap(*args,**kwargs):
        t1=time.time()
        func(*args,**kwargs)
        t2=time.time()
        return ("It took",str((t2-t1)*1000),"miliseconds")
    return wrap

class Person:
    def __init__(self,name,last_name,age,gender,student,password):
        self.name=name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.student=student
        self.__password=password

    @dec1
    def Greeting(self,second_person):
        return "Welcome dear "+second_person.name

    def Goodbye(self):
        return "Bye everyone!"

    def Favourite_num(self, num1):
        try:
            if type(num1)!=int:
                raise ValueError
            else:
                return ("My favourite number is",num1)
        except ValueError:
            return "The input isn't a number"

    def Read_file(self,filename):
        try:
            open(filename+".txt")
        except Exception:
            print("No such file exists")

    def setpassword(self,newpassword):
        self.__password=newpassword

    def getpassword(self):
        return self.__password

a=Person("Michael","Douglas",55,"Male",False,"sahsgdhksj")
b=Person("Ketrin","Zeta Jones",33,"Female",True,"nss,s.mxd")
a.Read_file("abcde")
print(a.Goodbye())
print(a.Favourite_num('a'))
print(a.Greeting(b))