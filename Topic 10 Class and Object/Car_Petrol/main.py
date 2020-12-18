from Car_Petrol.car import Car
from Car_Petrol.petrol_station import PetrolStation

opel = Car(50)
suzuki = Car(40)

shell = PetrolStation(5000)

#before Filling petrol
print("Opel before fuel "+ str(opel.capacity))
print("Shell fuel amount before fil " + str(shell.fuel_amount))

#OPEL car filling up petrol
shell.fill(opel)
print("Shell fuel amount after fill " + str(shell.fuel_amount))
print("Opel after fuel " +str(opel.capacity))

#SUZUKI car filling up petrol
shell.fill(opel)
print("Shell fuel amount after fill " + str(shell.fuel_amount))
print("Suzuki after fuel " + str(suzuki.capacity))


for i in range(0,10):
    opel.drive()