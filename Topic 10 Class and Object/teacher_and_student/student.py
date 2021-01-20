class Student:
    def __init__(self,name):
        self.name = name

    def learn(self):
        print (self.name, "learn something new!")

    def question(self,teacher):
        return teacher.answer()