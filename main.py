from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

my_car = Car('red', 3812.4)

color, mileage = my_car

print(color, mileage)

print(*my_car)

print('-------------')
Car = namedtuple('Car', 'color mileage')


class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'


my_car = MyCarWithMethods('red', 3812.4)
print(my_car.hexcolor())
