'''
# khai báo biến age = 12 tuổi
age = 22
# sử dụng điều kiện age <4 thì in ra cost is $0
if age < 4:
    print("Your admission cost is $0.")
# nếu age <18 thì in ra cost $25
elif age < 18:
    print("Your admission cost is $25.")
# nếu cả 2 cái đều sai thì in ra cost $40.
else:
    print("Your admission cost is $40.")
# các câu lệnh if được thực hiện từ trên xuống.

age = 12
if age < 4:
    # gán giá trị 0 vào biến price
    price = 0
elif age < 18:
    # gán giá trị 25 vào biến price
    price = 25
else:
    # gán giá trị 40 vào biến price
    price = 40
# in nội dùng với biến price sau khi đã so sánh bằng câu điều kiện if elif và else.
print(f"Your admission cost is ${price}.")
'''
# khai báo age
age = 66

if age < 4:  # so sánh age với giá trị 4
    price = 0           # gán price =0 nếu câu điều kiện đúng
elif age < 18:          # tiếp tục so sánh nếu age lớn hơn 4 và nhỏ hơn 18
    price = 25          # nếu age >4 và <18 thì gán price =25
elif age < 65:          # tiếp tục so sánh age nếu <65 và >18
    price = 40          # gán price =40 nếu age >18 and age <65
else:                   # nếu cả 3 if trên không thỏa thì gán price=20
    price = 20
# in ra giá cost sau khi xử lý các điều kiện ( lấy giá trị cuối cùng của price để xuất ra)
print(f"Your admission cost is ${price}.")
