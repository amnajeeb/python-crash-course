# Using if statements with lists, p.89

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print('Adding ' + requested_topping + '!')

print('\nFinished making your pizza!')

#

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('\nSorry we\'re out of green peppers right now.')
    else:
        print('\nAdding ' + requested_topping + '!')

print('\nFinished making your pizza!')

# Code above: ln.13 = these lines are inserted to inform that 'green peppers'
# are not available should green peppers be a requested topping (which it is).


requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print('\nAdding ' + requested_topping + '!')
    print('\nFinished making your pizza!')
else:
    print('\nAre you sure you want a plain pizza?')

# The code above checks first (ln.26) if the list is empty or not. If the list
# contains at least one item, Python assumes the statement as True (triggering
# the following operations ln.27-29). If list is empty, Python assumes the
# statement as False and jumps to else statement ln.30.

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']

requested_toppings = ['french fries', 'mushrooms', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('\nAdding ' + requested_topping + '.')  # True
    else:
        print('\nSorry we don\'t have ' + requested_topping + '.')  # False

print('\nFinished making your pizza')

# The code above checks that items in requested_toppings are part of
# available_toppings.
