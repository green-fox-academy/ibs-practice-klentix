# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
#
# Surface Area: 600
# Volume: 1000

length = float(input('please enter length: '))
width = float(input('please enter width: '))
height = float(input('please enter height: '))

#calculate SA
SA = 2*(length*width + length*height + width*height)
formattedSA =
print ('Surface Area :', "{:.2f}".format(SA))

#calculate Volume
Volume = length * width * height
print ('Volume:', "{:.2f}".format(Volume))
