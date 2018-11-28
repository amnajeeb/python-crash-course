players = ['magic', 'lebron', 'kobe']

# use of for LOOP to apply printing to each player within player variable.

for player in players:
    print(player)

# for LOOP has been defined, and each item from the 'players' loop has been
# stored in a new variable called 'player'.
# for every player in the players list
#   printout each name in the players list.


# when naming the for LOOP, it's best to use a name that represents a single
# item in the list. e.g. for player in players. for dog in dogs etc.

for player in players:
    print('Dear ' + player.title() + ', you\'ve been invited to our dinner')

# When creating a loop, any indented line under the loop is considered part
# of the loop. Multiple operations can thus be executed with one loop.

for player in players:
    print('Dear ' + player.title() + ', you\'ve been invited to our dinner')
    print('Looking forward to having you with us, ' + player.title() + '.')

# if the next operation within the loop is NOT indented, it will only be
# applied to the last item on the list (in the e.g. above: to Kobe only)
