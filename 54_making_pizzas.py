# Import hàm bằng cách import toàn bộ module
# Import mỗi một hàm riêng cần sử dụng


# Importing an Entire Module
# import file pizza1 được tạo cùng folder với file cần lấy sử dụng.
# lấy toàn bộ hàm trong file

# cú pháp from tên_module(file.py) import + Tên_funcitons
from pizza1 import makeSoda
# cú pháp import +tên module ( tên file.py)
import pizza1


# gọi hàm bằng cách tên_module.hàm_cần_gọi(tên biến)
pizza1.makePizza(16, 'pepperoni')
pizza1.makePizza(14, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions.
# import từ 1 file và lấy mỗi 1 hàm nếu chỉ sử dụng hàm đó
makeSoda('Medium', 'Ly nhựa')
