class Employee:
    def __init__(self, name, last_name, monthly_salary):
        self.name = name
        self.last_name = last_name
        self.__monthly_salary = monthly_salary
    def getFullName(self):
        print(self.name, self.last_name)
    def annualSalary(self):
        if self.__monthly_salary*12>100:
            print('High')
        else:
            print('Lower')

e=Employee('Karen', 'KK', 150)
e.getFullName()
e.annualSalary()