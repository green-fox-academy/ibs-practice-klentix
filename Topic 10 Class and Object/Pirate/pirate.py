import random


class Pirates:
    def __init__(self):
        self.name = name
        self.count = 0
        self.alive = True
        self.parrot = ""

    def drink_some_rum(self):
        self.count += 1
        return self.count

    def how_is_it_going_mate(self):
        if self.count <= 4 and self.alive:
            print("pour me anuddle")
        else:
            print("Arghh, I'ma Pirate. How dya dink its goin?")

    def die(self):
        self.alive = False

    def brawl(self,pirate):
        if self.alive == True:
            chance = random.random()
            if chance < 0.33:
                pirate.alive = False
            elif 0.33 <= chance <= 0.66:
                pirate.alive = False
                self.alive =  False
            elif chance > 0.66:
                pirate.alive = True

    def add_parrot(self,parrot):
        self.parrot = parrot







