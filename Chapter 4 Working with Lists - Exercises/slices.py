# Exercises Chapter 4, p.69

# 4-10
teams = ['Yankees', 'Red Sox', 'Orioles', 'Blue Jays', 'Rays', 'Mets']
print('The first three items in the list are:')
print(teams[0:3])
print('Three items from the middle of the list are:')
print(teams[1:4])
print('The last three items in the list are:')
print(teams[-3:])

# 4-11
pizzas = ['pepperoni', 'margherita', 'sicilian']
friends_pizzas = pizzas[:]

pizzas.append('hawaii')
friends_pizzas.append('french')

print('My favorite pizzas are')
print(pizzas)
print('My friend\'s favorite pizzas are')
print(friends_pizzas)

# 4-12
print("My favorite pizzas are:")
for item in pizzas:
    print(item.title())

print("My friend's favorite pizzas are:")
for item in friends_pizzas:
    print(item.title())
