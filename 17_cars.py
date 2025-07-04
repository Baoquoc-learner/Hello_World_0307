cars = ['audi', 'bmw', 'subaru', 'toyota']

# chạy for car để cho chạy từ audi tới toyota.
# kẹp thêm điều khiện if để khi nào car là bmw thì in ra BMW
# nếu car chạy trong for mà k phải bmw thì chỉ viết hoa ký tự đầu tiên.
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
