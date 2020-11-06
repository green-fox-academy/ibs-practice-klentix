#create a list
listA = ['Apple', 'Avocado', 'Blueberries', 'Durian', 'Lychee']

#create new list , same as list A

listB = listA.copy()
print("List B:" ,listB)

#Print out whether List A contains Durian or not
for item in listA:
    if item == 'Durian':
        print("There is Durian in list A")

#Remove Durian from List B
listB.pop(3)
print("List b after removing durian: ", listB)

#Add Kiwifruit to List A after the 4th element
listA.insert(3,'Kiwi')
print("List A after adding Kiwi: ",listA)

#Compare the size of List A and List B
if len(listA) == len(listB):
    print("List A and B have Same size")
elif len(listA) >  len(listB) or len(listB) > len(listA):
    print("List A and B do not have same size")

#Get the index of Avocado from List A
print("index of avocado in list A is :",listA.index('Avocado'))

#Get the index of Durian from List B
if 'Durian' not in listB:
    print('Durian is not in list B')

#Add Passion Fruit and Pomelo to List B in a single statement
listB.extend(['Passion Fruit','Pomelo'])
print(listB)

#Print out the 3rd element from List A
print("3rd element from list A: ", listA[2])