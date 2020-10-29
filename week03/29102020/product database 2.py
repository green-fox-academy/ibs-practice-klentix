proddb  = {"Eggs":200,
           "Milk":200,
           "Fish":400,
           "Apples":150,
           "Bread":50,
           "Chicken":550}

#Which products cost less than 201? (just the name)

for k,v in proddb.items():
    if v < 201:
        print(k)
#Which products cost more than 150? (name + price)

for k,v in proddb.items():
    if v > 150:
        print(k,v)