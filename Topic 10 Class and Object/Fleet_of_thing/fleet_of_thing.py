from fleet import Fleet
from thing import Thing

class FleetOfThing(Fleet,Thing):
    def __init__(self):
        super.__init__()
        print ("ok")






# - You have the `Thing` class
# - You have the `Fleet` class
# - You have the `fleet_of_things.py` file
# - Download those, use those
# - In the `fleet_of_things` file create a fleet
# - Achieve this output:
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

fleet = FleetOfThing()



fleet.add('Get milk')
fleet.add('Remove the obstacles')
fleet.add('Stand up')
fleet.add('Eat lunch')

tempthing = Thing('Get milk')
tempthing2 = Thing('Remove the obstacles')
tempthing3 = Thing('Stand up')
tempthing4 = Thing('Eat lunch')

print(fleet)
print(tempthing)