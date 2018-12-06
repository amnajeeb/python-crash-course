# Tuples, p.70

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# The code below (ln.10) is an attempt to modify the tuple. Should we try to
# print the tuple, it would return an error as tuples are immutable and cannot
# be modified.
# dimensions[0] = 100

for dimension in dimensions:
    print(dimension)

# One can write over a tuple. See example below (ln.17 to 25) with the tuple
# 'dimensions' being redefined.
dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (150, 25)
print('\nNew dimensions:')
for dimension in dimensions:
    print(dimension)
