class Teacher:
    def __init__(self,name):
        self.name = name

    def teach(self,student):
        return student.learn()

    def answer(self):
        print(self.name,"is answering a question")