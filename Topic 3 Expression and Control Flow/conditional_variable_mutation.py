a = 24
out = 0
# if a is even increment out by one
if a%2==0:
    print ('out',out+1)
else:
    print ('out',out)




b = 13
out2= ""
# if b is between 10 and 20 set out2 to "Sweet!"
if 10<b<20:
    out2 = ("sweet!")
# if less than 10 set out2 to "Less!",
elif b<10:
    out2 = ("less!")
# if more than 20 set out2 to "More!"
elif b>20:
    out2 = ("More!")
print(out2)



c = 123
credits = 100
is_bonus = False
# if credits are at least 50,
# and is_bonus is false decrement c by 2
# if credits >= 50 and is_bonus == False:
if credits >= 50 and not is_bonus
    print('c=', c-2)


# if credits are smaller than 50,
elif credits <50 and not is_bonus
    print('c=',c-1)
# and is_bonus is false decrement c by 1
# if is_bonus is true c should remain the same






d = 8
time = 120
out3 = ""
# if d is dividable by 4
# and time is not more than 200
# set out3 to "check"
# if time is more than 200
# set out3 to "Time out"
# otherwise set out3 to "Run Forest Run!"

if d%4==0 and time == 200:
    print (out3,"check")
elif time >200:
    print (out3,"timeout")
else:
    print (out3,"run forest run!")
print(out3)