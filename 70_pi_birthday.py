# Reading from a file
# Is Your Birthday Contained in Pi?


from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Nhập ngày sinh cảu bạn theo dạng mmddyy: ")
if birthday in pi_string:
    print("Có xuất hiện ngày sinh của mày trong 1 triệu số pi đầu tiên")
else:
    print("Đéo có xuất hiện ngày sinh của mày")
