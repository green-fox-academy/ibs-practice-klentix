key = int()
value = str()
print("key:", key)
print("value:", value)

key = (97,98,99,65,66,67)
value = ('a','b','c','A','B','C')
print("Key: ", key)
print("Value: ", value)

map = {"97":"a",
       "98":"b",
       "99":"c",
       "65":"A",
       "66":"B",
       "67":"C"}

#add on another set of value
map["68"] =("D")
print (map)

# show number of item in a dict
print("total number of key value pair: ", len(map))

# show value that was mapped with certain item
print("value that map with 99 is ", map.get("99"))

# remove key value
map.pop("97")
print(map)

#print where if there is such pair
print("if there is value of 100: ", map.get("100"))

#remove all key value
map.clear()
print("map after removing all: ",map)