# hiệu chỉnh, thêm vào, xóa đi các yếu tố trong python
brand_clothes = ['karants', 'mikenko', '5theway', 'nike']
# print(brand_clothes)

brand_clothes[1] = 'adidas'
brand_clothes.append('prada')
brand_clothes.append('dirty_coin')
print(brand_clothes)

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

del famous_people[1]
del famous_people[2]
print(famous_people)
