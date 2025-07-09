# in đầy đủ tên bằng 2 biến gán vào 1 biến tổng quát. dùng lệnh f format
firtsName = "tran bao"
lastName = "quoc"
fullName = f"{firtsName} {lastName}"
print(fullName)
print(fullName.title())
print(fullName.upper())
print(fullName.lower())


message = f"Hello, {fullName.title()}!"
print(message)

print(f"Hello, {fullName.title()}!")
