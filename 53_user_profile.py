# Using Arbitrary Keyword Arguments
# dùng - đối số từ khóa tùy ý

def buildProfile(first, last, **userInfo):
    """tạo 1 thư viện bao gồm mọi thứ mà ta biết về người dùng """
    userInfo['FirstName'] = first
    userInfo['LastName'] = last
    return userInfo


userProfile = buildProfile(
    'albert', 'enstein', Location='princeton', Field='physics', Age=25)
print(userProfile)
