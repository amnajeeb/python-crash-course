pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print(pizza)

# Summarize the order
print('You ordered a ' +
      pizza['crust'] +
      '-crust pizza with the following toppings:')

for topping in pizza['toppings']:  # IMPORTANT: Use loop to print values.
    print('\t' + topping.capitalize())


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'edward': ['ruby', 'python'],
    'phil': ['python', 'haskell']
    }

for names, languages in favorite_languages.items():
    print('\n' + names.title() + '\'s favorite language(s) are:')
    for language in languages:
        print('\t' + language.title())
print('...')

# ln.24: one way to remember which method to use when looping dictionaries:
# if you use keys & values ---> for key, value in dictionary.items()
# if you use keys only ---> for key in dictionary.keys()
# if you use values only ---> for value in dictionary.values()

# IMPORTANT REMINDER: ln.26: Because some of the values in dictionary
# favorite_languages are lists, to print those values, we need a loop to print
# items within these lists. Otherwise, the list (with brackets and commas) will
# be printed.

for names, languages in sorted(favorite_languages.items()):
    if len(languages) > 1:
        print('\n' + names.title() + '\'s favorite languages are:')
        for language in languages:
            print('\t' + language.title())
    else:
        print('\n' + names.title() + ' likes only one language:')
        for language in languages:
            print('\t' + language.title())
