def func(password):
    error=0
    #password = input('Enter a password: ')
    passlength = len(password)
    if passlength<10:
        error += 1 
        print(False)
    elif sum(map(str.isdigit, password)) < 2:
        error += 1
        print(False)
    else:
        print(True)

func('qddjq12gnt')