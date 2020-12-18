class Animal:
    hunger = 0
    thirst = 0

    def __init__(self):
        self.hunger = 50
        self.thirst = 50

    def drink(self):
        self.thirst -= 1
        print('has drunk! ' + 'Thirst level: ' + str(self.thirst))
    def eat(self):
        self.hunger -= 1
        print('has eaten! ' + 'Hunger level: ' + str(self.hunger))
    def play(self):
        self.thirst += 1
        self.hunger += 1
        print( 'is happy! ' + 'Thirst level: ' + str(self.thirst) + ' Hunger level: ' + str(self.hunger))
tiger = Animal()
print('Tiger default mode: '
      + '\n Hunger: ' + str(tiger.hunger)
      + '\n Thirst: ' + str(tiger.thirst))

tiger.eat()
tiger.drink()
tiger.play()
tiger.play()

rabbit = Animal()
print('\nRabbit default mode: '
      + '\n Hunger: ' + str(rabbit.hunger)
      + '\n Thirst: ' + str(rabbit.thirst))
rabbit.eat()
rabbit.drink()
rabbit.play()


