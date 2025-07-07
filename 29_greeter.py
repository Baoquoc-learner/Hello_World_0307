# Nhập tên và xuất ra bằng function input()
name = input("Please enter your name:")
print(f"\nHello, {name.title()}!")

print("\t--------------------------------------------------")

# += Là thêm dòng lệnh đó vào sau dòng trước đó.
promt = "If you share your name, we can personalize the messages you see."
promt += "\nWhat is your first name? "

name = input(promt)
print(f"Hello, {name}!")

print("\t--------------------------------------------------")

# Dùng kiểu dữ liệu số thực integer.
age = input("How old are you?")
age = int(age)
print(age)
