# - Create a variable named `animals`
#   with the following content: `["koal", "pand", "zebr"]`
# - Add all elements an `"a"` at the end

animals = ["koal", "pand", "zebr"]
def addona(animals):
    for i in animals:
        return[i+"a" for i in animals]

print(addona(animals))