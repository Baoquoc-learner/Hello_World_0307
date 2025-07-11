# The __init__() Method for a Child Class
# tạo một lớp con từ phương thức init

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometerReading = 0

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometerReading} miles on it.")

    def updateOdometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometerReading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)


myLeaf = ElectricCar('nissan', 'leaf', 2024)
print(myLeaf.getDescriptiveName())
myLeaf.incrementOdometer(200)

myLeaf.readOdometer()
