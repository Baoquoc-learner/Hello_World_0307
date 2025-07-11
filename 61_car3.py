# Modifying an Attribute's Value Through a Method
# điều chỉnh giá trị thuộc tính qua 1 phương thức


class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # Tạo giá trị odometerReading =0
        self.odometerReading = 22

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def readOdometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometerReading} miles on it.")
    """
    def updateOdometer(self, mileage=3):
        #Set the odometer reading to the given value.
        self.odometerReading = mileage
    """

    def updateOdometer(self, mileage):
        """
        Set the odometer reading to the give value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometerReading:
            self.odometerReading = mileage
        else:
            print("You can't roll back an odometer!")


myNewCar = Car('audi', 'a4', 2024)
print(myNewCar.getDescriptiveName())

myNewCar.updateOdometer(21)
myNewCar.readOdometer()
