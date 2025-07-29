# Exceptions
# The Else Block
''' Khối Else'''
print("Give me two Numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("Nhập số tử đi bạn: ")
    if first_number == 'q':
        break
    second_number = input('Nhập số mẫu đi bạn: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
