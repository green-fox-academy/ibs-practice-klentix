students = [
        {'name': 'Mark', 'age': 9.5, 'candies': 2},
        {'name': 'Sean', 'age': 10, 'candies': 1},
        {'name': 'Clark', 'age': 7, 'candies': 3},
        {'name': 'Paul', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies
import collections
def who_has_more_candies(students):
    c = collections.Counter()
    for entry in students:
        if entry['candies'] > 4:
            c.update(entry)
    print ("who has more than 4 candies:",dict(c)['name'])

who_has_more_candies(students)

# create a function that takes a list of students and prints:
#  - how many candies they have on average

def average_candy(students):
    vals = [student['candies']for student in students]
    #print(vals)
    average = sum(vals)/len(vals)
    print("average candies:", average)

average_candy(students)
