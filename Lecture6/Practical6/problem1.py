class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def getDesc(self):
        print('A ' + self.color,'circle with radius ', self.radius)

c=Circle(15,'blue')
c.getDesc()