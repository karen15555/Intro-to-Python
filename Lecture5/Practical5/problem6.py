def keywordarg(user,**kwarg):
    if user=="admin":
        for x,y in kwarg.items():
            print(x,":",y)
        else:
            print("access denied to user "+user)

keywordarg("admin",a=15,b=4)

keywordarg("Name",a="15",b="4")