import productcheck
def buy(product, num, price):
    if productcheck.check(product,num):
        print("You bought",product,"and spent",num*price)
    else:
        print("Sorry! We are out of this product.")

def main():
    buy("candy",10,15)
if __name__=='__main__':
    main()