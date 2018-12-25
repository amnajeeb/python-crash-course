user_0 = {
    'username': 'mrivera',
    'first': 'mariano',
    'last': 'rivera',
    }

for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

# The .items() method is used to go through the list of key-value pairs.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print('\n' + name.title() + "\'s favorite language is:")
    print(language.title())

# Code above: ln.20: we defined two variables, 'name' and 'language' which are
# the key and value from dictionary favorite_languages.

for name in favorite_languages.keys():  # Using the method .keys() is optional.
    print(name.title())

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:  # ensure that name is in friends.
        print('Hi ' + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

# Code above: ln.35. Translation: if name is in variable friends, print
# following message.

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')
else:
    print('Thanks for taking the poll Erin!')

# Code above: ln.43 checks if erin is among the keys in favorite_languages
# dictionary.

for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll!')

# Looping through all the values (only) in a list.

print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())

# Code above will return all values (stored in language variable) from
# favorite_languages dictionary. This will include duplicate. To prevent this,
# we can use the set() function. See below.

print('\nThe following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
