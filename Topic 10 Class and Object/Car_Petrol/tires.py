class Tires:
    wear = 0

    def __init__(self):
        self.wear = 0

    def drive(self):
        self.wear += 1

    def is_usable(self):
        #a tire is usable when it less than 10 times
        return self.wear < 10
