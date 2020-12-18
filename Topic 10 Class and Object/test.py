class Point3D(object):
    def __init__(self,a,b,c):
        self.x = a
        self.y = b
        self.z = c
    def __repr__(self):
        return "Point3D(%d, %d, %d)" % (self.x, self.y, self.z)
    def __str__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)
my_point = Point3D(1, 2, 3)
print (my_point) # __repr__ gets called automatically
print (my_point) # __str__ gets called automatically**