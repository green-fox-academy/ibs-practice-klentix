proddb  = {"Eggs":200,
           "Milk":200,
           "Fish":400,
           "Apples":150,
           "Bread":50,
           "Chicken":550}

#How much is the fish?
print("fish price: ", proddb.get('Fish'))

#What is the most expensive product?
sort_product = sorted(proddb.items(), key =
             lambda kv:(kv[1], kv[0]))
print("The most expensive product:", sort_product[0])

#What is the average price?
average = sum(proddb.values())/len(proddb)
print("Average price: ", average)

#How many products' price is below 300?
for k,v in proddb.items():
    if v < 300:
        print(k,v)

#Is there anything we can buy for exactly 125?
for k,v in proddb.items():
    if v % 125 == 0:
        print(k,v)
    else:
        print("nothing we can buy for exactly 125")
    break

#What is the cheapest product?
sort_product = sorted(proddb.items(), key =
             lambda kv:(kv[1], kv[0]))
print("The cheapest product:", sort_product[-1])