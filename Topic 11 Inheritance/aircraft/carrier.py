from aircraft import Aircraft,F16,F35

class Carrier:
    def __init__(self,hp,total_damage):
        self.aircrafts = []
        self.ammo = 2300
        self.hp = 5000
        self.total_damage = 2280

    def add(self,aircraft):
        self.aircrafts.append(aircraft)

    def fill(self):
        ammo_needed =  0
        for i in self.aircrafts:
            ammo_needed += (i.max_ammo - i.ammo)
            try:
                if self.ammo < ammo_needed:
                    if i.isPriority:
                        remaining = i.refill(self.ammo)
                        self.ammo += remaining
                for i in self.aircrafts:
                    remaining = i.refill(self.ammo)
                    self.ammo += remaining

            except:
                print("Run out of ammo")

    def fight(self,carrier):
        for i in self.aircrafts:
            carrier.hp -= i.fight()

    def getStatus(self):
        if self.hp <= 0:
            return "It's dead Jim :("
        else:
            return f"THP: {self.hp}, Aircraft count: {len(self.aircrafts)}, Ammo Storage: {self.ammo}, Total damage: {self.total_damage}"
            for i in self.aircrafts:
                return f"Type {i.__class__.__name__}, Ammo: {i.ammo}, Base Damage: {i.base_damage}, All Damage: {i.damage}"

