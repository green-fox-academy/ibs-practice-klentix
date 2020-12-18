class PetrolStation:
    fuel_amount = 0

    def __init__(self,fuel_amount):
        self.fuel_amount = fuel_amount

    def fill(self, car):
        difference = car.capacity - car.fuel_amount
        car.fuel_amount = car.capacity
        self.fuel_amount -= difference