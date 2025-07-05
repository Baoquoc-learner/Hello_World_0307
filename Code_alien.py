alienColor = ['green', 'yellow', 'red']
# 5.3 alien color#1

if alienColor == 'green':
    print("The player just earned 5 points.")
else:
    print("You died")

print("\t ----------------------------------------------")

# 5.4 alien color#2
if alienColor == 'green':
    print("The player just earned 5 points for shooting the alien")
if alienColor != 'green':
    print("The player just earned 10 points.")

print("\t ----------------------------------------------")

# 5.5 alien color#3
for alien in alienColor:
    if alien == 'green':
        print("The player just earned 5 points")
    if alien == 'yellow':
        print("The player just earned 10 points")
    if alien == 'red':
        print("The player just earned 15 points")

print("\t ----------------------------------------------")
