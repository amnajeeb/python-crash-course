# Storing your functions in modules p.154


def make_pizza(type, size, *toppings):
    """Creates a pizza base on user input"""
    print("You've picked a " + type.title() + " pizza, " + "size " +
          size.upper() + ", with the following toppings: ")
    for topping in toppings:
        print("\t- " + topping.title())
