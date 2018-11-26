# Changing, adding, removing elements in a list, p.40

motorcycles = ['triumph', 'honda', 'suzuki', 'yamaha']
print(motorcycles)

motorcycles[3] = 'ducati'
print(motorcycles)

# the .append() method is used to add items to a list
# (i.e. it will be added at the end)

motorcycles.append('yamaha')
print(motorcycles)

ale_teams = []
ale_teams.append('Yankees')
print(ale_teams)
ale_teams.append('Red Sox')
print(ale_teams)
ale_teams.append('Rays')
print(ale_teams)

# the .insert(, ) method is used to add items to a list.
# note that position within the list must be specified before the item.
# e.g. list.insert(0, 'item')

rankings = ['Lakers', 'Blazers', 'Clippers']
print(rankings)
rankings.insert(0, 'Warriors')
print(rankings)

# deleting an item is done with the del statement (!!! not a method)
# the del statement appears before the list name
# the item position must be added to the list

del rankings[1]
print(rankings)

# Lakers were removed from the rankings list.

# the pop() method can be used to remove the last item in a list,
# but preserving that item (rather than deleting completely).

motorcycles = ['honda', 'yamaha', 'ducati']
last_owned = motorcycles.pop()

print('The last motorcycle I owned was a '+last_owned.title()+'.')

world_series_champions = ['Royals', 'Cubs', 'Astros']
world_series_champions.append('Red Sox')
last_winners = world_series_champions.pop()
print('The last team to win the World Series was the '+last_winners+'.')

# The pop() method can be used to remove a specific item by adding
# the position inside the parentheses

motorcycles = ['honda', 'yamaha', 'ducati']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a '+first_owned.title()+'.')

# The remove() method can be used to remove an item based on its value
# This method only removes the first occurence in a list

al_east = ['Yankees', 'Red Sox', 'Rays', 'Orioles', 'Blue Jays']
world_series_winner = 'Red Sox'
al_east.remove(world_series_winner)
print(al_east)
