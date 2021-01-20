from station import Station
from car import Car

honda = Car('honda')
bhp = Station('bhp')

print("honda current gas amount:", honda.gas_amount)
print("honday capacity:", honda.capacity)

print("bhp gas amount:",bhp.gas_amount)

bhp.refill_car(honda)
print("bhp after refill:", bhp.gas_amount)
print("honda after refill:", honda.gas_amount)
print("honday capacity:", honda.capacity)