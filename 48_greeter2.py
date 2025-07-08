

def getFormattedName(firstName, lastName):
    """Return a full name, neatly formatted."""
    fullName = f"{firstName} {lastName}"
    return fullName.title()


# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    fName = input("First name: ")
    if fName == 'q':
        break
    lName = input("Last name: ")
    if lName == 'q':
        break
    formattedName = getFormattedName(fName, lName)
    print(f"\nHello, {formattedName}!")
