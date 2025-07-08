# Avoiding Argument Errors

def describe_pet(animalType, petName):
    """Display information about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"My {animalType}'s name is {petName.title()}.")


describe_pet('dog', 'Lucix')
