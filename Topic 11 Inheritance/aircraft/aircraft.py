class Aircraft:
    def __init__(self):
        self.name = name
        self.ammo = 0
        self.max_ammo = 0
        self.base_damage = 0
        self.damage = 0

    def fight(self):
        self.ammo = 0
        self.damage = self.base_damage * self.ammo
        return self.damage

    def refill(self,num):
        ammo_needed = self.ammo - self.max_ammo
        if ammo_needed < num:
            self.ammo += ammo_needed
        elif ammo_needed > num:
            self.ammo += num
        return self.ammo


    def getType(self):
        return self.name

    def getStatus(self):
        print ("Type " + self.name + " Ammo: " + str(self.ammo) +
               " Base Damage: " + str(self.base_damage) + "All Damage: " + str(self.damage))

    def isPriority(self):
        if self.name == "F35":
            return True
        else:
            return False


class F16(Aircraft):
    def __init__(self):
        self.name = "F16"
        self.ammo = 8
        self.max_ammo = 8
        self.base_damage = 30

class F35(Aircraft):
    def __init__(self):
        self.name = "F35"
        self.ammo = 12
        self.max_ammo = 12
        self.base_damage = 50
