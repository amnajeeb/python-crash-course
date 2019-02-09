# Returning a simple value p.142


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formated."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# ln.7: translation: the function would take arguments (in our case 'jimi' and
# 'hendrix') and return them as output defined in ln.7 (i.e. with .title()).
# ln.10: when you call a function that returns a value, you MUST use a variable
# to store the return value (the full_name variable is only for the sake of the
# function definition)


def get_formatted_name1(first_name, last_name, middle_name=''):
    """Return a full name, neatly formated."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


athlete = get_formatted_name1('kobe', 'bryant', 'bean')
print(athlete)

# Code above: ln.20, we're using an optional parameter should we need a middle
# name. We assign no value to the parameter middle_name and we put it at the
# end of the list of arguments.
# ln.22: we've reformatted the full name depending on whether we have a value
# for middle name or not.
