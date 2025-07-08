# Positional Arguments

def describePet(animalType, petName):
    """Display information about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"My {animalType}'s name is {petName.title()}.")


describePet('hamster', 'johnSon')

print("\t--------------------------------------------------")
# Multiple Function Calls: gọi nhiều hàm cùng lúc.


def describe_pet(animalType, petName):
    """Display information about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"My {animalType}'s name is {petName.title()}.")


# Khai báo cho chạy các hàm.
describe_pet('Cat', 'Jenny')
describe_pet('dog', 'Lucifer')

print("\t--------------------------------------------------")
# Order Matters in Positional Arguments


def describePet(animalType, petName):
    """Display information about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"My {animalType}'s name is {petName.title()}.")


describePet('harry', 'hamster')

print("\t--------------------------------------------------")
print("\t--------------------------------------------------")

# Keyword Arguments


def describe_pet(animalType, petName, age):
    """Display information about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"My {animalType}'s name is {petName.title()}.")
    print(f"My pet's age is {age}")


describe_pet(petName='harry', age=25, animalType='hamster')
