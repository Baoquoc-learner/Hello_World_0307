dimensions = (200, 50, 123)
# dimensions[0] = 155   # sai cú pháp
# print(dimensions[0])
# print(dimensions[1])
# print(dimensions[2])
# List khác tuple ở chỗ định nghĩa hay gọi là cú pháp là dấu ngoặc.
# Đối với list thì dùng [], List có thể thay đổi giá trị đưuọc
# Đối với tuple thì dùng (), tuple là bất biến không thể thay đổi giá trị được
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (3004, 1111, 607)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
