# Returning a dictionary p.144


def build_person(first_name, last_name, age=''):
    """return a dictionary of information about a person"""
    person = {'first': first_name,
              'last': last_name,
              }
    if age:
        person['age'] = age
    return person


athlete = build_person('lebron', 'james')
print(athlete)

# Code above: this function actually creates a dictionary based on the
# input information at ln.14.
# ln.14: even though we've defined a dictionary ln.6, it is only for the sake
# of the function definition. We still have to define a dictionary on ln.14 to
# store the information.
# IMPORTANT you can not assign a method to (e.g. .title()) to person at ln.11
# because it is a dictionary. To be able to use a method, one has to define
# the key-value pair to which the method will be applied (e.g. person['last'])
# ln.9: we introduce that condition should the user add his/her age, then we'd
# create another key-value pair with age.
