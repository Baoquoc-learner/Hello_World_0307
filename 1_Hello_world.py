# bài 1: hello world
'''
print("Hello_world")
'''
# Bài 2: variables

# in bằng gán string vào 1 biến
'''
message = "Hello anh Thắng ăn hại"
print(message)

message = "Hello anh Thắng ăn hại và ăn hai"
print(message)

mesage = "Hello Python Crash Course reader!"
print(mesage)
'''
# in chữ với nội dung là title, in hoa chữ cái đầu của mỗi từ
'''
name = "ADA lovelace"
print(name.title())
'''
# in đầy đủ tên bằng 2 biến gán vào 1 biến tổng quát. dùng lệnh f format
'''
firts_name = "tran bao"
last_name = "quoc"
full_name = f"{firts_name} {last_name}"
'''
# in nội dung của biến đã được format.
'''
message = f"Hello, {full_name.title()}!"
print(message)

print(f"Hello, {full_name.title()}!")
'''
# in ra nội dung với \t là cách vào và \n là xuống dòng.
'''
print("python\t là một\n ngôn ngữ\n dễ học\n dể sử dụng")
'''
# rstrip là lệnh để xóa khoảng trắng phía sau của dòng string.
# lstrip là lệnh để xóa khoảng trắng phía trước của dòng string.
# strip là lệnh để xóa khoảng trắng cả trước và sau.
'''
favorite_language = 'python  '
favorite_language = favorite_language.rstrip()
'''
# Lệnh removeprefix có chức năng là xóa string trùng với nội dung string cần xóa.
'''
nostarch_url = 'htt://anhthangchianhailagioi.com'
print(nostarch_url.removeprefix('htt://'))
'''
# luyện tập try it yourself
'''
name_eric = "Hello Eric, would you like to learn some Python today?"
print(name_eric)

first_name = "ho quy"
last_name = "thang lol"
full_name = f"{first_name} {last_name}"
print(full_name.lower())
'''
''''
AE_speak = '"A person who never made a mistake never tried anything new"'
author = "Albert Einstein"
print(author.title(), "once said:", AE_speak)

famous_person = "Albert Einstein"
message = '"A person who never made a mistake never tried anything new"'

print(famous_person.title(), f"once said:\n".title(), message.title())
'''
# về số numbers
'''
# print(4/2.0)
universe_age = 14_000_000_000
print(universe_age)
#gán nhiều biến
x, y, z = 16, 88, 15
print((x+y)/z)
# biến có các từ viết hoa toàn bộ là hằng số không nên thay đổi
MAX_CONNECTIONS = 5000
'''
# Bài 3: list
'''
# tạo biến vietcontrol trong đó có nhiều nội dung.
vietcontrol = ['BCV_V1', 'BCV_V2', 'BCV_V3', 'IMS', "DLR"]
message = f"my firts bagcounter is {vietcontrol[2].upper()}"
print(message)
'''
# hiệu chỉnh, thêm vào, xóa đi các yếu tố trong python
'''
brand_clothes = ['karants', 'mikenko', '5theway', 'nike']
#print(brand_clothes)

brand_clothes[1] = 'adidas'
brand_clothes.append('prada')
brand_clothes.append('dirty_coin')
print(brand_clothes)
'''
# thêm vào cuối list dùng append
famous_people = []
famous_people.append('Putin')
famous_people.append('9Pham')
famous_people.append('ToLam')
# print(famous_people)
# Thêm vào vị trí đã chỉ định dùng insert
famous_people.insert(1, 'PV_Giang')
# print(famous_people)

# Xóa 1 nội dung ở trong list
'''
del famous_people[1]
del famous_people[2]
print(famous_people)
'''
