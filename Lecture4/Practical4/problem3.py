name = str(input())
age = int(input())
password = input()


    if name == "Batman":
    print("Welcome Mr. Batman!")
else:

    if age<16:
        print("Dear " + name + ", you are too young to register")
    if "*" not in password and "&" not in password:
        print("Please enter a different password")

#other way to do
if age<16 and name =="Batman":
    pass
else:
    print("Dear " + name + ", you are too young to register")
if "*" not in password and "&" not in password:
    print("Please enter a different password")
if name == "Batman":
    print("Welcome Mr. Batman!")
if age<16 and "*" not in password and "&" not in password and name == "Batman":
    print("Welcome Mr. Batman!")