class Person:
    def __init__(self,name = "Jane Doe ",age = 30,gender ="female" ):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("hi, I'm " + self.name , ", a " + str(self.age) +"year old " + self.gender)

    def get_goal(self):
        print ("My goal is: Live for the moment!")

