import random
from pirate import Pirates

class Ship:
    def __init__(self):
        self.pirates = []
        self.captain = None

    def fill_ship(self):
        if self.captain == None:
            captain = Pirates()
            self.captain = captain
        for i in range(1,random.randint(3,7)):
            pirates = Pirates()
            self.pirates.append(pirates)

    def info(self):
        count_alive = 0
        captain_alive = ""
        for i in self.pirates:
            if i.alive:
                count_alive +=1
        if self.captain.alive:
            captain_alive = "is alive"
        else:
            captain_alive = "is dead"
        return count_alive,captain_alive
