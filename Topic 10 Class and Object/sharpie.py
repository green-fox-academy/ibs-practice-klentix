class Sharpie:
    color = str()
    width = int()
    ink_amount = int()

    def __init__(self):
        self.ink_amount = 100

    def use(self):
        self.ink_amount -= 20.5
        if self.ink_amount <= 1:
            print('No more ink')
        else:
            print('sharpie has been used, balance: ' + str(self.ink_amount))

sharpie1 = Sharpie()
sharpie1.color = 'pink'
sharpie1.width = 2.5

print('Sharpie 1 details: '
      + '\n color: '+ sharpie1.color
      + '\n width: '+ str(sharpie1.width)
      + '\n ink amount: '+ str(sharpie1.ink_amount))

sharpie1.use()
sharpie1.use()
sharpie1.use()
sharpie1.use()
sharpie1.use()
sharpie1.use()
sharpie1.use()
sharpie1.use()
