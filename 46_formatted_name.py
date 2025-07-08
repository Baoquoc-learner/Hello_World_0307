
def get_formattedName(firstName, lastName):
    # Returning a Simple Value
    # trả về một giá trị đơn giản
    """Trả về tên đầy đủ, được định dạng gọn gàng."""
    fullName = f"{firstName} {lastName}"  # Kết hợp tên
    return fullName.title()  # Trả về tên đã được chuyển đổi sang Title Case


# Gọi hàm và gán giá trị trả về vào biến 'musician'
musician = get_formattedName('jimi', 'hendrix')
print(musician)  # In ra giá trị của biến 'musician'

print("\t--------------------------------------------------")

# Making an Argument Optional
# Biến đổi số thành tùy chọn


def get_formattedName(firstName,  lastName, middleName='',):
    """Return a full name, neatly formatted."""
    if middleName:
        fullName = f"{firstName} {middleName} {lastName}"
    else:
        fullName = f"{firstName} {lastName}"
    return fullName.title()


# trả về kết quả không có tên đêm. vì thứ tự khai báo bên dưới
# có First name và last name, không có middle name thì câu if sẽ chuyển sang else
musician = get_formattedName('jimi', 'hendrix')
print(musician)
# ở dưới có cả first, last, middle name nên là if true:
# tại đây trong hàm sẽ trả về kết quả return được gán vào musician.
musician = get_formattedName('dfghj', 'lee', 'hooker')
print(musician)
