# Using countinue in a loop

currentNumber = 0
while currentNumber < 20:
    currentNumber += 1
    if currentNumber % 2 == 0:
        continue

    print(currentNumber)
