
# Using Arbitrary Keyword Arguments
# dùng đối số từ khóa tùy ý

def buildProfile(first, last, **userInfo):
    """tạo 1 thư viện bao gồm mọi thứ mà ta biết về người dùng 
        bao gồm tên, họ và thông tin thêm
    """
    userInfo['FirstName'] = first
    userInfo['LastName'] = last
    return userInfo


# userProfile = buildProfile('albert', 'enstein', Location = 'princeton', Field = 'physics', Age = 25)
userProfile = buildProfile('albert', 'einstein', age=25, field='Physics')

print(userProfile)
# print(userProfile.get('LastName', 'khong co nha'))
# thông tin thêm vào như location hay field hay age
# là thông tin thêm của người dùng có thể có hoặc không
