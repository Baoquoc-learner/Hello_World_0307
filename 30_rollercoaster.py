# Using int() to accept Numerical Input

height = input("How tall are you, in inches? ")
# height = '475'
height = float(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
