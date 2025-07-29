# Reading from a File

# Reading the contents of a File
'''Đọc nội dùng của một file'''
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
# print(contents)

# Relative and Absolute File Paths
'''
Nói về cách gán biến Path tương đối hoặc tuyệt đối
ví dụ:
path = Path ('Python_0307/pi_digits.txt')   # đường dẫn tương đối

path = Path ('D:/2024-2026_SPKT/Python_0307'/pi_digits.txt) # Đường dẫn tuyệt đối
'''
# Accessing a File's Lines
'''Truy cập một dòng trong một file'''
contentss = path.read_text()
lines = contentss.splitlines()
for line in lines:
    print(line)
