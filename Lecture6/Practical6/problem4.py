class Car:
    def __init__(self, model, color, max_speed):
        self.model = model
        self.color = color
        self.max_speed = max_speed
    def compareCar(self, car2):
        if self.max_speed>car2.max_speed:
            print("car1 is better than car2")
        else:
            print("car2 is better than car1")

c=Car('Lexus', 'White', 250)
c1=Car('BMW', 'Blue', 150)

c.compareCar(c1)