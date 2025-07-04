banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
# nếu biến user không có trong list banned_users thì in ra nội dùng print().
# Làm quen với cây lệnh if và các comment điều kiện so sánh.
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
