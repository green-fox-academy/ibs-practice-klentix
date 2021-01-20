from animal import Animal

class Farm:
    def __init__(self):
        self.animals = []
        self.slot = 50

    def add(self,name):
        self.animals.append(name)
        return self.animals

    def breed(self):
        if len(self.animals) < self.slot:
            animal = Animal()
            self.add(animal)

    def slaughter(self):
        hunger = 0
        least_hungry = None
        for i in self.animals:
            if i.get_hunger() > hunger:
                least_hungry = i
                hunger = i.get_hunger()

        for i in self.animals:
            if i == least_hungry:
                self.animals.remove(i)

    def get_animals(self):
        return self.animals
