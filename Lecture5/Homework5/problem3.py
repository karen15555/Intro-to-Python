def dec(f):
    def wrap(*args,**kwargs):
        print("Before function call")
        print(f(*args,**kwargs))
        print("After the function call")
    return wrap
@dec
def myfunc():
    return "Inside the function"
myfunc()