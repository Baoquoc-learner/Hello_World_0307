# removing All Instances of Specific Values form a List.

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', ' rabbit', 'cat']
print(pets)

while 'dog' in pets:
    pets.remove('dog')
while 'cat' in pets:
    pets.remove('cat')
print(pets)
