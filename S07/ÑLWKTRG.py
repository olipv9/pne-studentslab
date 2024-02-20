class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0
        brand += 'TM'

    def set_speed(self, speed):
        self.speed = speed
        self.brand += 'TM'

    def get_speed(self):
        return self.speed


my_car = Car('renault')
print(my_car.get_speed())
my_car.set_speed(80)
print(my_car.get_speed())


