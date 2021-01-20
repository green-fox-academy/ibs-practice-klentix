from person import Person

class Mentor(Person):
    def __init__(self,name = "Jane Doe ",age = 30 ,gender = "female",level = "Intermediate"):
        super().__init__(name,age,gender)
        self.level = level

    def get_goal(self):
        print ( "Educate brilliant junior software developers.")

    def introduce(self):
        print ("Hi, I'm " + self.name +", a " + str(self.age)+ " year old " + self.gender +" " + self.level +" mentor.")

