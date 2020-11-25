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

print('------- build in function -------')
import json
print(my_car._asdict())
print(json.dumps(my_car._asdict()))
your_car = my_car._replace(color='blue')
print(your_car)
print(your_car.hexcolor())