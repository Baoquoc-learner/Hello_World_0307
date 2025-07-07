alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
alien_3 = {'color': 'purple', 'points': 20}

aliens = [alien_0, alien_1, alien_2, alien_3]
for alien in aliens:
    print(alien)

print("\t--------------------------------------------------")

# Make an empty list for storing aliens.
aliens = []
for alienNumber in range(30):
    alienNew = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(alienNew)
# Show the first 5 aliens.
for alien in aliens[:2]:
    print(alien)
print("...")

# show how many aliens have been created.
print(f"Total number of Aliens: {len(aliens)}")

print("\t--------------------------------------------------")

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alienNumber in range(30):

    alienNew = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(alienNew)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)

print("...")
