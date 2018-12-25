# Start of Chapter 6 - Dictionaries, p.96

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print('\nYou\'ve just earned ' + str(alien_0['points']) + ' points!')

new_points = alien_0['points']  # We're selecting this key within alien_0

print(str(new_points))

# Adding more key-value pairs, by simply defining a new key-value pair (no
# need to use a method.

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Creating a new dictionary starting from an empty one.

alien_1 = {}

alien_1['color'] = 'blue'
alien_1['points'] = 10
alien_1['x_position'] = 5
alien_1['y_position'] = 35

print(alien_1)

# Changing the value of a key

print('\nThe alien color is ' + alien_1['color'] + '.')  # color defined ln.26

alien_1['color'] = 'red'
print('\nThe alien color has changed and is now ' + alien_1['color'] + '.')

# Using loops to modify alien position

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x-position: " + str(alien_2['x_position']))

# Moving alien_2 to the right
# Determine how far to move the alien based on its current speed

if alien_2['speed'] == 'slow':
    x_increment = 1  # x_increment is a variable !
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment

alien_2['x_position'] = alien_2['x_position'] + x_increment

print("\nNew position: " + str(alien_2['x_position']))

# deleting a key-value pair PERMANENTLY

alien_0 = {'color': 'green', 'points': 5}

del alien_0['color']
print(alien_0)
