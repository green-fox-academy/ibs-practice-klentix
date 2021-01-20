class Cohort:

    name = ''
    students = []
    mentors = []

    def __init__(self,name):
        self.name = name
        self.students = []
        self.mentors = []

    def add_students(self,Student):
        self.students.append(Student)
        return self.students

    def add_mentors(self,Mentor):
        self.mentors.append(Mentor)
        return self.mentors

    def info(self):
        print("The " + self.name +" cohort has " + str(len(self.students)) +
              " students and " + str(len(self.mentors)) +" mentors.")

