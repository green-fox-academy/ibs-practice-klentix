from Car_Petrol import tires

class Car:
    fuel_amount = 0
    capacity = 0

    def __init__(self, capacity):
        # providing default value for every new car
        self.fuel_amount = 10
        self.capacity = capacity
        self.tires = [Tires(),Tires(),Tires(),Tires()]

    def drive(self):
        if self.fuel_amount == 0:
            print('no fuel,car is not drivable')
            return
        for tire in self.tires:
            if not tire.is_usable():
                print ('Tire is not usable')
                return
        self.fuel_amount -= 1
        for tire in self.tires:
            tire.drive()

        print ("driving the car")