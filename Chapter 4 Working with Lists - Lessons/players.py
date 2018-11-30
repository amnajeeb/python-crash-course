# Working with part of a list, p.65


# ln.6: selection is only for items 0,1,2. Item 3 is NOT included.
players = ['Kobe', 'LeBron', 'Shaq', 'Magic', 'Larry']
print(players[0:3])


# if the first index is omitted, the selection will start at the first item
# by default. See below.
points = list(range(2, 6))
print(points[:3])

# if the first index is omitted, the selection will start at the first item
# by default. See below.
rebounds = list(range(2, 6))
print(rebounds[0:])

# if the first index is negative and the 2nd one is empty, the selection will
# start at the end of the list and move from the beginning. See below.
teams = ['Yankees', 'Red Sox', 'Orioles', 'Blue Jays', 'Rays']
print(teams[-5:])

teams = ['Yankees', 'Red Sox', 'Orioles', 'Blue Jays', 'Rays']
print('Here are the first three teams in the standings:')
for item in teams[0:3]:
    print(item)
