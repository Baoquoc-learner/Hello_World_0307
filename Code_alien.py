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

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print("\t ----------------------------------------------")

available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")
