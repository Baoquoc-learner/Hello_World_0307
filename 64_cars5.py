# Defining Attributes and Methods for the Child Class
# xác định các thuộc tính và phương thức cho lớp con.
# tạo class Car
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


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vahicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        #Khởi tạo thuộc tính của lớp cha ( lớp ban đầu Car)
        Then initialize attributes specific to an electric car.
        #Khởi tạo cụ thể thuộc tính vào  class electricCar
        """
        super().__init__(make, model, year)
        self.batterySize = 40

    def describeBattery(self):
        """Print a statement describing the battery size."""
        # in một câu lệnh mô tả kích thước của pin
        print(f"This car has a {self.batterySize} -kWh battery.")

    def updateOdometer(self, mileage):
        return super().updateOdometer(mileage)


myLeaf = ElectricCar('nissan', 'leaf', 2024)

print(myLeaf.getDescriptiveName())
myLeaf.describeBattery()
myLeaf.updateOdometer(250)
myLeaf.readOdometer()
