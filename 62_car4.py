# Incrementing an Attribute's Value Through a Method
# Tăng giá trị thuộc tính của một phương thức.

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # Tạo giá trị odometerReading =0
        self.odometerReading = 0

    def detail(self):
        detail2 = f"{self.year} {self.make} {self.model} {self.odometerReading}"
        return detail2.title()

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def readOdometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometerReading} miles on it.")

    def updateOdometer(self, mileage):
        # Set the odometer reading to the given value.
        self.odometerReading = mileage

    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometerReading += miles


myUsedCar = Car('subaru', 'sport', 2020)
print(myUsedCar.getDescriptiveName())
print(myUsedCar.detail())
myUsedCar.updateOdometer(23_200)
myUsedCar.readOdometer()

myUsedCar.incrementOdometer(800)
myUsedCar.readOdometer()
