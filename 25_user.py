# Looping Through a Dictionary
# Looping Through All Key-Value Pairs
user_0 = {
    'username': 'seazwan',
    'first': 'eric',
    'last': 'cantona',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

for key in user_0.keys():
    print(f"\nKey: {key}")

for value in user_0.values():
    print(f"\nValue: {value}")

languages = {'python', 'rust', 'python', 'c'}
print(languages)
