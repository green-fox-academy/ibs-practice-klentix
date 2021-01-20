from person import Person
from student import Student
from mentor import Mentor
from sponsor import Sponsor
from cohort import Cohort

def main():

    people = []

    mark = Person('Mark', 46, 'male')
    people.append(mark)
    jane = Person()
    people.append(jane)
    john = Student('John Doe', 20, 'male', 'BME')
    people.append(john)
    student = Student()
    people.append(student)
    gandhi = Mentor('Gandhi', 148, 'male', 'senior')
    people.append(gandhi)
    mentor = Mentor()
    people.append(mentor)
    sponsor = Sponsor()
    elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
    people.append(elon)
    student.skip_days(3)

    for i in range(5):
        elon.hire()

    for i in range(3):
        sponsor.hire()

    for person in people:
        person.introduce()
        person.get_goal()

    awesome = Cohort('AWESOME')
    awesome.add_students(student)
    awesome.add_students(john)
    awesome.add_mentors(mentor)
    awesome.add_mentors(gandhi)
    awesome.info()



if __name__ == '__main__':
    main()