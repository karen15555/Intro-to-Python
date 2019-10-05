class Police_car:
    def __init__(self, owner, price, pass_code):
        self.owner = owner
        self.price = price
        self.__pass_code = pass_code
    tax_value = 0.2
    def tax(self):
        print(self.tax_value*self.price)
    def greeting(self):
        if self.__pass_code =='admin':
            print('Welcome to your car,',self.owner,'!')

c=Police_car('Anton', 79000, 'admin')
c.tax()
c.greeting()
