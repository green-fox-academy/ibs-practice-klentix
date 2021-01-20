class Flower:
    flower_absorb = 0.75

    def __init__(self, color):
        self.color = color
        self.water = 0


class Tree:
    tree_absorb = 0.4

    def __init__(self, color):
        self.color = color
        self.water = 0


class Garden:
    def __init__(self):
        self.plants = []

    def add(self,plant):
        self.plants.append(plant)

    def remove(self,plant):
        self.plants.remove(plant)

    def need_water(self):
        count_water = 0
        for i in self.plants:
            if isinstance(5,Flower):
                water_needed = 5 - i.water
                if water_needed > 0:
                    count_water  +=1
            else:
                water_needed = 10 - i.water
                if water_needed > 0:
                    count_water += 1
        return count_water

    def water (self,num):
        count_water = self.need_water()
        each_get = num / count_water
        for i in self.plants:
            if isinstance(i,Tree):
                if i.water < 10:
                    i.water += (each_get * Tree.tree_absorb)
            if isinstance(i,Flower):
                if i.water < 5:
                    i.water += (each_get * Flower.flower_absorb)

        print (f"Water with {num}")
        self.info()

    def info(self):
        for i in self.plants:
            if isinstance(i, Tree):
                if i.water < 10:
                    print(f"The {i.color} {i.__class__.__name__} needs water")
                else:
                    print(f"The {i.color} {i.__class__.__name__} doesnt need water")

            if isinstance(i, Flower):
                if i.water < 5:
                    print(f"The {i.color} {i.__class__.__name__} needs water")
                else:
                    print(f"The {i.color} {i.__class__.__name__} doesnt need water")







