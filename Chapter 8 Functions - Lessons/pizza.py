# Passing an arbitrary number of arguments p.151


def make_pizza(*toppings):
    """print the list of toppings for a pizza"""
    print("Here are the toppings you've chosen for your pizza: ")
    for topping in toppings:
        print("\t- " + topping.title())


make_pizza('pepperoni')
make_pizza('pepperoni', 'cheese', 'pineapple')

# ln.4: the * symbol used with the parameter is used to indicate that we can
# use an arbitrary number of arguments when calling the function. We did just
# that lanes 11 & 12 when we had a different number of arguments.


def pizza_type(size, *toppings):
    """Asks user to confirm size and toppings for pizza"""
    print("\nYou've ordered a " + size.upper().strip() +
          " pizza and the following toppings:")
    for topping in toppings:
        print("\t- " + topping.title().strip())


pizza_type('large', 'pepperoni', 'cheese', 'mushrooms')

# ln.19: If we want to have a parameter with an open number of arguments, this
# parameter should be placed at the end of all parameters when defining the
# function.
