
# A simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print("\t--------------------------------------------------")
# Working With Dictionaries
# Accessing Values in a Dictionary
alien_1 = {'color': 'yellow', 'points': 10}
print(alien_1['color'])
newPoints = alien_1['points']

print(f"You just earned {newPoints}.points!")

print("\t--------------------------------------------------")
# Adding New Key-Value Pairs
alien_2 = {'color': 'red', 'points': 15}
print(alien_2)
alien_2['x_position'] = 0
alien_2['y_position'] = 25
print(alien_2)

print("\t--------------------------------------------------")
# Starting with an Empty Dictionary
alien_3 = {}
alien_3['color'] = 'purple'
alien_3['points'] = 20
print(alien_3)

print("\t--------------------------------------------------")

# Modifying Values in a Dictionary
alien_4 = {'color': 'white'}
print(f"The Alien is {alien_4['color']}.")
alien_4['color'] = 'black'
print(f"The Alien is now {alien_4['color']}.")

print("\t--------------------------------------------------")

alien_5 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_5['x_position']}")
alien_5['speed'] = 'fast'
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_5['speed'] == 'slow':
    x_increment = 1
elif alien_5['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3   # This must be a fast alien.
# The new position is the old position plus the increment.
alien_5['x_position'] = alien_5['x_position'] + x_increment
print(f"New position: {alien_5['x_position']}")

print("\t--------------------------------------------------")

# Removing Key-Value Pairs.
alien_6 = {'x_position': 0, 'y_position': 50, 'speed': 'medium'}
print(alien_6)

del alien_6['speed']
print(alien_6)
del alien_6['x_position']
print(alien_6)

print("\t--------------------------------------------------")

# A Dictionary of Similar Objects
favoriteLanguages = {
    'jenni': 'python3',
    'thang': 'C++',
    'quoc': 'C#',
    'binh': 'SQL'
}
language = favoriteLanguages['quoc'].title()
print(f"Quốc's favorite Language is {language}.")

print("\t--------------------------------------------------")

# Using get() to Access Values
alien_7 = {'color': 'green', 'speed': 'slow'}
point_value = alien_7.get('points', 'Không có đâu mà get mẹ gì.')
print(point_value)

print("\t--------------------------------------------------")
