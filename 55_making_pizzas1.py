# Using as to Give a Function an Alias
# dùng alias để viết tắt tên module

import pizza1 as pi
from pizza1 import makePizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', ' extra cheese')

# cú pháp from module_name funciton_name as fn
# module_name là tên file, funciton_name là tên hàm chức năng, fn là tên viết tắt của hàm

# Using as to Give a Module an Alias
# Dùng alias để viết tắt cho tên module.

pi.makePizza(16, 'tiêu đen')
pi.makePizza(24, 'peppers', 'cheese', 'chilibell')
