# Removing all instances of specific values from a list.

pets = ['snake', 'cat', 'dog', 'hamster', 'golden fish', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Using the while loop is useful here to ensure that we remove ALL instances
# of 'cat' in the pets list.
