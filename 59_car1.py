# Setting a Default Value for an Attribute
# cài đặt giá trị mặc định cho một thuộc tính

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # Tạo giá trị odometerReading =0
        self.odometerReading = 0

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def readOdometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometerReading} miles on it.")


myNewCar = Car('audi', 'a4', 2024)
print(myNewCar.getDescriptiveName())
myNewCar.readOdometer()
