cars = ['ferrari', 'toyota', 'nissan', 'citroen']
cars.sort()
print(cars)

# The argument reverse=True (note the capital T) is used to reverse the
# alphabetical order

cars.sort(reverse=True)
print(cars)

cars = ['ferrari', 'toyota', 'nissan', 'citroen', 'mistubishi']
print('Here\'s the original list: ')
print(cars)
print('\nHere\'s the sorted list: ')

# use of the sorted() FUNCTION to sort the list without modifying the list
# itself. Note that the list is within the function.

print(sorted(cars))

# The .reverse() method permanently reverses the order of a list (i.e. not
# alphabetically, only the order).

cars.reverse()
print(cars)
cars.reverse()
print(cars)

# the len() function is used to determine the number of items in a list.

print(len(cars))
