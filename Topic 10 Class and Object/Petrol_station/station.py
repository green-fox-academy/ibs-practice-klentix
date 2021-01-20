from car import Car

class Station:
    def __init__(self, name):
        self.name = name
        self.gas_amount = 1000

    def refill_car(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount = car.capacity
        return self.gas_amount
