# Tạo module để khi sử dụng thì import vào chương trình main

# tạo pizza theo yêu cầu
def makePizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# tạo hàm làm soda với size và kiểu


def makeSoda(size1, style):
    print(f"\nSize {size1} và loại ly {style}.")
