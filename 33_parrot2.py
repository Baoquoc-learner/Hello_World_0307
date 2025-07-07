# Letting the User Choose When to Quit

promt = "\nTell me something, and I will repeat it back to you:"
promt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(promt)
    if message != 'quit':
        print(message)
