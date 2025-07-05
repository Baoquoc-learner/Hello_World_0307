# lệnh sort dùng để sắp xếp theo thứ tự A-Z trong list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # với cars.sort() là sắp xếp theo thứ tự A-Z
# với cars.sort(reverse=true) là đảo ngược cách sắp xếp từ Z-A
cars.sort(reverse=True)
print(cars)
print("\t-----------------")
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# cars.reverse() ## cũng là 1 cách đảo sắp xếp từ Z-A
# print(cars)
