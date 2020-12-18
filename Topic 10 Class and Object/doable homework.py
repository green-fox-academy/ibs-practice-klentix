#Create 5 trees
#Store the data of them in variables in your program
#for every tree the program should store its'
#type
#leaf color
#age
#sex
#you can use just variables, or lists and/or maps

# christmas_tree = ['pine tree','green',4,'male']
# beech_tree = ['beech','brown',15,'female']
# oak_tree = ['oak','red',4,'male']

class tree:
    type = ''
    leaf_color = ''
    age = 0
    gender = ''

    def __init__(self,type,leaf_color,age,gender):
        self.type = type
        self.leaf_color = leaf_color
        self.age = age
        self.gender = gender

christmas_tree = tree('pine','green',4,'female')
print('type ' + christmas_tree.type)
print('leaf color ' + christmas_tree.leaf_color)
print ('age ' + str(christmas_tree.age))
print ('gender ' + christmas_tree.gender)

beech_tree = tree('beech','brown',24,'male')
print('type ' + beech_tree.type)
print('leaf color ' + beech_tree.leaf_color)
print ('age ' + str(beech_tree.age))
print ('gender ' + beech_tree.gender)