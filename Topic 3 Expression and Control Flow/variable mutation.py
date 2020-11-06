a = 3
# make the "a" variable's value bigger by 10
a += 10
print('a=',a)

##################
b = 100
# make b smaller by 7
b -= 7
print('b=',b)

##################
c = 44
# please double c's value
c *= 2
print('c=',c)

##################
d = 125
# please divide by 5 d's value
d /=5
print('d=',d)

##################
e = 8
# please cube of e's value
e **=3
print('e=',e)


##################
f1 = 123
f2 = 345
# tell if f1 is bigger than f2 (pras a boolean)
if f1 > f2:
    print ('f1 is bigger than f2')
else:
    print ('f1 is smaller than f2')

##################
g1 = 350
g2 = 200
# tell if the double of g2 is bigger than g1 (pras a boolean)
if (g2*2) > g1:
    print ('double of g2 bigger than g1')
else:
    print ('double of g2 is not bigger than g1')

##################
h = 1357988018575474
# tell if 11 is a divisor of h (pras a boolean)
x = 11
def isDivisible(h, x):
    return h % x == 0
print ('if 11 is a divisor of h:',isDivisible(h,x))

##################
i1 = 10
i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)

if i1 > i2**2 and i1 < i2**3:
    print ('i1 is higher than i2 squared and smaller than i2 cubed ')
else:
    print ('false')

##################
j = 1521
# tell if j is divisible by 3 or 5 (pras a boolean)
m = 3
n = 5
def isDivisible(j, m):
    return j % m == 0
print ('if 1521 is a divisble by 3:',isDivisible(j,m))

def isDivisible(j, n):
    return j % n == 0
print ('if 1521 is a divisble by 5:',isDivisible(j,n))