# Passing a List
# bỏ qua danh sách

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


userNames = ['hannah', 'meymey', 'erina', 'Thắng', 'Quốc', 'Bình']
greet_users(userNames)
