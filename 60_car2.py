# Modifying Attribute Values
# Chỉnh sữa giá trị của thuộc tính có 3 cách
# Modifying an Attribute’s Value Directly
# sửa đổi trực tiếp giá trị của thuộc tính
# tạo class Car:
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
# in hàm getDescriptiveName ra
myNewCar.odometerReading = 24

# gán giá trị 23 vào biến odometerReading trong Class Car
myNewCar.readOdometer()
# Cho khởi tạo hàm readOdometer() với biến Car với 3 thuộc tính đã cài sẵn
