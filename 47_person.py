# Making an Argument Optional

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)

# returning a Dictionary
# trả về giá trị là một thư viện


def buildPerson(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musicianPerson = buildPerson(first_name='Nuna', last_name='Nunan', age=28)
print(musicianPerson)
