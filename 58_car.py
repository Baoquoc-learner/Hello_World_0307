# Working with Classes and Instances
# làm việc với class và các trường hợp
# Tạo lớp Car

class Car:
    """A simple attempt to represent a car"""
    # hàm __init__ sẽ tự động khởi tạo với giá trị được gán vào
    # hàm __init__ phải đủ 3 giá trị: make , model, year

    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def getDescriptiveName(self):
        """Return a neatly formatted descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

# Gán giá Car với 3 giá trị tham số cần thiết.


myNewCar = Car('audi', 'a4', 2025)
print(myNewCar.getDescriptiveName())
# in ra myNewCar với các giá trị đã khai báo ban đầu.
