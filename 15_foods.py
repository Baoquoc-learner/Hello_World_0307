# khai báo biến my_foods với 3 items
my_foods = ['pizza', 'falafel', 'carrot cake']
# khai báo biến friend_foods bằng cách gán giá trị của biến My-foods
# Có thể chọn giá trị gán bất kì trong my_foods bằng cách [] ghi nhận giá trị trong ngoặc vuông
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
