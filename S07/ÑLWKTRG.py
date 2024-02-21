class Car:
    def __init__(self, brand,speed=0):
        self.brand = brand
        self.speed = speed
        brand += 'TM'

    def set_speed(self, speed):
        self.speed = speed
        self.brand += 'TM'

    def get_speed(self):
        return self.speed


class Ferrari (Car):
    def __init__(self):
        super().__init__('ferrari', 100)
        # Esto lo que hace es q coge todas las características del init de arriba, de la main class,
        # y se las añade porque como depende de la clase de arriba necesita tener los mismos
        # atributos, después ya puedes añadir extras que sean caraterísticos de la sub-clase.
        self.music = 'classic'

    def make_cabrio(self):
        self.speed = 20
        self.music = 'loud'
        return 'WOW'


my_car = Car('renault')
yourcar = Ferrari()
print(yourcar.brand)
yourcar.set_speed(120)
print(yourcar.speed)
print(yourcar.make_cabrio(), 'and music is', yourcar.music, 'and speed', yourcar.speed)



