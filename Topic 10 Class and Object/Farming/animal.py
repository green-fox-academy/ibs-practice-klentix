class Animal:


    def __init__(self):
        self.hunger = 50
        self.thirst = 50

    def drink(self):
        self.thirst -= 1
        return self.thirst
    def eat(self):
        self.hunger -= 1
        return self.hunger

    def play(self):
        self.thirst += 1
        self.hunger += 1
        return self.thirst, self.hunger

    def get_hunger(self):
        return self.hunger

    def get_thirst(self):
        return self.thirst



