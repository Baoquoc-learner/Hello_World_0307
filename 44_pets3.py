
# Gọi các hàm tương tự nhưng cho 1 kết quả
# Định nghĩa hàm describePet
def describePet(petName, animalType='dog'):
    """Display information about a pet."""  # Đây là docstring, mô tả chức năng của hàm
    # Đây là thân hàm, chứa các câu lệnh thực hiện công việc của hàm
    print(f"\nI have a {animalType}.")
    print(f"My {animalType}'s name is {petName.title()}.")


# A dog named Willie. (Các lời gọi này nằm ngoài và sau khối def)
describePet('willie')
describePet(petName='willie')

# A hamster named Harry.
describePet('harry', 'hamster')
describePet(petName='harry', animalType='hamster')
describePet(animalType='hamster', petName='harry')
