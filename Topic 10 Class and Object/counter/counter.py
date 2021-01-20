class Counter:
    value = int()

    def __init__(self):
        self.value = 0

    def addMore(self):
        self.value = eval(input('key in number here:')) + self.value
        print('Added one, current balance: ' + str(self.value))

    def addOne(self):
        self.value += 1
        print('Added one, current balance: ' + str(self.value))

    

    def get(self):
        print('Current: '+ str(self.value))

    def reset(self):
        self.value = 0
        print ('Reset to intial value: ' + str(self.value))

start = Counter()
print(start.value)
start.addOne()
start.get()
start.reset()
