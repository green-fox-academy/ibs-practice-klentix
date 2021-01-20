from sharpie import Sharpie

class Sharpieset:
    def __init__(self):
        self.sharpie = []

    def add(self,sharpie):
        self.sharpie.append(sharpie)

    def count_usuable(self):
        counter = 0
        for i in self.sharpie:
            if i.get_ink() > 0:
                counter += 1
        return counter

    def remove_trash(self):
        for i in self.sharpie:
            if i.get_ink() <= 0:
                self.sharpie.remove(i)
                return self.sharpie

    def get_sharpie(self):
        return self.sharpie