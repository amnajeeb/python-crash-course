# Exercises p.108

# 6.4

glossary = {}

glossary['list'] = 'range of number'
glossary['tuple'] = 'immutable list'
glossary['statement'] = 'checks condition of interest'
glossary['integer'] = 'other name for number in programming'
glossary['set'] = 'list of unique items within a dictionary'
glossary['dictionary'] = 'list of items or attributes organised in key-value'

for term, definition in sorted(glossary.items()):
    print(term.title() + ':')
    print(definition.capitalize() + '.')

# ln.12: 'term' is defined for keys; 'definition' is defined for values.

# 6.5

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'gange': 'india',
    'mekong': 'cambodia',
    'yangtze': 'china',
    }

for river, country in sorted(rivers.items()):
    print('The ' + river.title() + ' runs through ' + country.title() + '.')

print('\n')

for river in sorted(rivers.keys()):
    print(river.title())

print('\n')

for country in sorted(rivers.values()):
    print(country.title())

# 6.6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

names = [
    'robert',
    'sarah',
    'jess',
    'ines',
    'benny',
    'phil',
    'jen',
    'edward'
    ]

print('\n')

for name in sorted(names):
    if name not in favorite_languages.keys():
        print('Can you take 5 minutes to take our poll, ' +
              name.title() + '?')
    else:
        print('Thanks for taking our poll, ' + name.title() + '!')

# VERY IMPORTANT: the loop has to go through names in 'names', not in
# favorite_languages.keys()!!! See ln.65.
# NB: Because the loop goes through name, if we want to sort the names by
# alphabetical order, sorted() has to be applied to the variable names!
