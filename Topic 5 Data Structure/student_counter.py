students = [
        {'name': 'Theodor', 'age': 3, 'candies': 2},
        {'name': 'Paul', 'age': 9.5, 'candies': 2},
        {'name': 'Mark', 'age': 12, 'candies': 5},
        {'name': 'Peter', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'George', 'age': 10, 'candies': 1}
]

# create a function that takes a list of students and prints:
# - how many candies are owned by students altogether

def total_candy(students):
    total = 0
    for student in students:
        total += student['candies']
    print("total candy: " + str(total))

total_candy(students)

# create a function that takes a list of students and prints:
# - The sum of the age of people who have less than 5 candies

import collections
def sum_age(students):
    c = collections.Counter()
    for entry in students:
        if entry['candies'] < 5:
            c.update(entry)
    print ("sum of age of student who have less than 5 candies:",dict(c)['age'])

sum_age(students)

