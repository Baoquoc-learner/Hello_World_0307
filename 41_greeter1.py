# Defining a Funciton
def greetUser():
    """Display a simple greeting."""
    print("Hello!")


greetUser()

print("\t--------------------------------------------------")

# Passing Information to a Funciton


def greetUser(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greetUser('Jesu')
