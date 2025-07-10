# Creating the Dog Class

class Dog:
    """ detail about a dog"""

    def __init__(self, name, age):
        # self là biến bắt buộc đứng đầu tiên
        # self sẽ xử lý và dùng cho các hàm ở dưới __init__
        """khởi tạo các thuộc tính như tên và tuổi của object"""
        """ __init__ là phương thức cố định"""
        # mỗi khi gọi Dog thì python sẽ tự động chạy __init__
        self.name = name
        self.age = age

    def sit(self):
        """Mô phỏng một con chó ngồi để đáp lại một mệnh lệnh."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Mô phỏng cuộn qua để đáp ứng với một lệnh."""
        print(f"{self.name} rolled over!")

    def bark(self):
        print(f"{self.name} is barking to me")
# Making an Instance from a Class
# tạo ví dụ về class


myDog = Dog(age=9, name='William Sharkbear')
print(f"My Dog's name is {myDog.name}.")
print(f"My Dog is {myDog.age} years old.")

myDog.sit()
myDog.roll_over()
myDog.bark()
