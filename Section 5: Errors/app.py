from numpy import isin


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):  # if car that provided from user is not an instance
            raise TypeError(
                f'Tried to add `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
        self.cars.append(car)


# ford = Garage()
# car = Car('Ford', 'Fiesta')
# ford.add_car(car)
# print(len(ford))

ford = Garage()
fiesta = Car('Ford', 'Fiesta')
try:
    ford.add_car('fiester')
except TypeError:
    print('Your car was not a Car!')
except ValueError:
    print('Something weird happened...')
finally:
    print(f'The garage now has {len(ford)} cars,')

# try except, else, else is for the code when there is no error
