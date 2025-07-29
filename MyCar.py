# importing a single class page 174
from cars8 import *
myNewCar = Car('Audi', 'a4', 2024)
print(myNewCar.getDescriptiveName())
myNewCar.odometerReading = 24
myNewCar.readOdometer()

print("\t--------------------------------------------------")
print("\t--------------------------------------------------")

myLeaf = ElectricCar('nissan', 'leaf', 2024)
print(myLeaf.getDescriptiveName())
myLeaf.battery.describeBattery()
myLeaf.battery.getRange()

print("\t--------------------------------------------------")
print("\t--------------------------------------------------")
