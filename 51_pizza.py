# Passing an Arbitrary Number of Arguments
# tạo và in ra list với biến *toppings đưuọc cho sẵn.
# vỡi *topping là dang tuple không đổi được, dấu ngoặc tròn
def makePizza(*toppings):
    """In danh sách topping được yêu cầu """
    print(toppings)


makePizza('pepperoni')
makePizza('mushrooms', 'green peppers', 'extra cheese')


print('\t--------------------------------------------------')
# tạo ra 1 list được viết theo for in dùng để in từ trên xuống theo thứ tự


def makePizza(*toppings):
    ''' Summarize the pizza we are about to make'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


makePizza('pepperoni')
makePizza('mushrooms', 'green peppers', 'extra cheese')


print("\t--------------------------------------------------")

# Mixing positional and Arbitrary Arguments.
# Kết hợp đối số vị trí và đối số tùy ý


def make_pizza(size, *toppings):
    """Tóm tắt chiếc pizza mà chúng ta sắp làm."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(18, 'pepperoni')
make_pizza(22, 'mushrooms', 'green peppers', 'extra cheese')
