# Importing Classes
# Importing a Single Class
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
            return self.odometerReading
        else:
            print("You can't roll back an odometer!")

    def incrementOdometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometerReading += miles


class Battery:
    """A simple attempt to model a battery for an electric car. """

    def __init__(self, batterySize=40):
        """Initialize the battery's attributes."""
        # khởi tạo thuộc tính của pin
        self.batterySize = batterySize

    def describeBattery(self):
        """Print a statement describing the battery size."""
        # in ra mô tả của pin
        print(f"This car has a {self.batterySize} -kWh battery.")

    def getRange(self):
        """Print a statement about the range thí battery provides."""
        if self.batterySize == 40:
            range = 150
        elif self.batterySize == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def detail(self):
        print(f"This car has a 222 -kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    # Đại diện cho các khía cạnh của một chiếc xe, cụ thể cho xe điện

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Khởi tạo các thuộc tính của lớp cha
        Then initializae attributes specific to an electric car.
        Sau khi khởi tạo sẽ gán vào xe điện
        """
        super().__init__(make, model, year)
        self.battery = Battery()
