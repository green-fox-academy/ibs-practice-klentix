shoplist = {"Milk":1.07,
            "Rice":1.59,
            "Eggs":3.14,
            "Cheese":12.60,
            "Chicken Breast":9.40,
            "Apples":2.31,
            "Tomato":2.58,
            "Potato":1.75,
            "Onion":1.10
            }

BobList = {"Milk":3,
           "Rice":2,
           "Eggs":2,
           "Cheese":1,
           "Chicken Breast":4,
           "Apples":1,
           "Tomato":2,
           "Potato":1
           }

AliceList = {"Rice":1,
             "Eggs":5,
             "Chicken Breast":2,
             "Apples":1,
             "Tomato":10
             }

#How much does Bob pay?
total =sum(shoplist[k]*BobList[k] for k in BobList)
print("Bob bought: ", total)  #how to ignore value that cannot be look up like 'onion'

#How much does Alice pay?
total2 =sum(AliceList[k]*shoplist[k] for k in AliceList)
print ("Alice bought: ", total2)

#different things between 2 buying list
keys1 = BobList.keys()
keys2 = AliceList.keys()
difference =  keys1 -keys2
print("Extra products purchase between two list:",difference)

#who buys more different prod
Bobcount = len(BobList)
Alicecount = len(AliceList)
if Bobcount > Alicecount:
    print("Bob bought more prods than Alice")
else:
    print("Alice bought more prods than Bob")

#Who buys more products? (piece)
b = sum(BobList.values())
a = sum(AliceList.values())
if b > a:
    print ("Bob buys more pieces ")
else:
    print("Alice buys more pieces")

#Who buys more Rice?
#Who buys more Potato?