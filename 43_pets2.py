# Default Values, cài giá trị mặc định cho biến

def describePet(petName, animalType='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"My {animalType}'s name is {petName.title()}.")


describePet('willie')
