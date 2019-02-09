# Using a function with a while loop p.145


def get_formatted_name(first_name, last_name):
    """return a full name neatly formated"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


# Infinite loop
while True:
    print('\nPlease tell me your name')
    print("Press 'q' to quit at any time")
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello, " + formatted_name + "!")
