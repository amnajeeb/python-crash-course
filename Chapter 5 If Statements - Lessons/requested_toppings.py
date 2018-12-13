# Testing multiple conditions, p.87

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

# Using multiple ifs statements (as opposed to if/elif ones) enables to
# verify multiple conditions, i.e. to verify if more than one condition
# can be true. In the example above, had we used elif statements, only the
# mushrooms would have been added. By using ifs several times, we can ensure
# that mushrooms AND extra cheese are added to the pizza.
