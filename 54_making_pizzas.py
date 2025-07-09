# Importing an Entire Module
# import file pizza1 được tạo cùng folder với file cần lấy sử dụng.
# lấy toàn bộ hàm trong file

from pizza1 import makeSoda
from pizza1 import makePizza
import pizza1

pizza1.makePizza(16, 'pepperoni')
pizza1.makePizza(14, 'mushrooms', 'green peppers', 'extra cheese')


# Importing Specific Functions.
# import từ 1 file và lấy mỗi 1 hàm nếu chỉ sử dụng hàm đó

makePizza(16, 'pepper')
makePizza(12, 'mushrooms', 'green peppers')


makeSoda('Medium', 'Ly nhựa')
