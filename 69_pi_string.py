# Reading from a file
# Working with a File's Contents
''' Làm việc với nội dung file'''
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

# Large Files: One Million Digits
'''Các tệp file lớn: 1 triệu chữ số'''
paths = Path('pi_million_digits.txt')
Contents = paths.read_text()
Lines = Contents.splitlines()
pi_String = ''
for Line in Lines:
    pi_String += Line.lstrip()

print(f"{pi_String[:52]}...")
print(len(pi_String))
