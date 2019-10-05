def dec1(func):
    def wrap(*args,**kwargs):
        return func(*args,**kwargs)+", it's me!"
    return wrap

def dec2(func):
    def wrap(*args,**kwargs):
        return "<u>"+func(*args,**kwargs)+"</u>"
    return wrap
@dec2
@dec1
def myfunc():
    return "Hi"
print(myfunc())