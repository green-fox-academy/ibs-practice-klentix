class Sharpie:


    def __init__(self,color= '',width= float()):
        self.ink_amount = 100
        self.color = color
        self.width = width


    def use(self):
        self.ink_amount -= 20.5
        if self.ink_amount <= 1:
            print('No more ink')
        else:
            print('sharpie has been used, balance: ' + str(self.ink_amount))

    def get_ink(self):
        return self.ink_amount

    def get_color(self):
        return self.color

    def get_width(self):
        return self.width


#
# sharpie1 = Sharpie()
# sharpie1.color = 'pink'
# sharpie1.width = 2.5
#
# print('Sharpie 1 details: '
#       + '\n color: '+ sharpie1.color
#       + '\n width: '+ str(sharpie1.width)
#       + '\n ink amount: '+ str(sharpie1.ink_amount))
#
# sharpie1.use()
# sharpie1.use()
# sharpie1.use()
# sharpie1.use()
# sharpie1.use()
# sharpie1.use()
# sharpie1.use()
# sharpie1.use()
