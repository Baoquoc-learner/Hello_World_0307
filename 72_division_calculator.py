# Exceptions
# Handling the ZeroDivisonError Exception.
'''Xử lý ngoại lệ lỗi ZeroDivisonError'''

# print(5/0)  # lỗi không chia được cho số 0

# Using try-expect Blocks
'''Sử dụng các khối try-except'''
print("Give me two Numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input('Nhập số tử đi ba: ')
    if first_number == 'q':
        break
    second_number = input('Rảnh thì nhập mẫu giùm: ')
    if second_number == 'q':
        break
    answer = float(first_number) / float(second_number)
    print(answer)
