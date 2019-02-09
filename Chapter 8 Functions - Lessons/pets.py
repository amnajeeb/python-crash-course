# Positional Arguments, p.136

# Positional arguments


def describe_player(name, team, position):
    """Description of player with name and team"""
    print(name.title() + " is a " + position +
          " who played for " + team.title() + ".")


describe_player('ronaldo', 'real madrid', 'striker')
describe_player('paolo maldini', 'a.c. milan', 'defender')

print('\n')

# Code above:
# ln.6: we've put multiple parameters: name, team & position.
# ln.12: we've matched the number of parameters (3) with 3 arguments.
# IMPORTANT: the order of arguments must match the order of parameters. In our
# code above, the first argument must be a name, then team, then position.

# Keyword arguments


def describe_team(name, city):
    """Description of NBA teams with name and city"""
    print("The " + name.title() + " are a basketball team based in " +
          city.title() + ".")


describe_team(city='brooklyn', name='nets')
describe_team(name='lakers', city='los angeles')
print('\n')

# ln.32: we're using keyword arguments, which enables us to forego the need to
# list arguments in the same order as parameters define ln.26.


# Default values


def describe_game(name, platform='playstation'):
    """Description of a video game with name and platform"""
    print(name.title() + " is a video game released on the " +
          platform.title() + ".")


describe_game('silent hill')
describe_game('resident evil 4', 'gamecube')

# ln.43: we've set what is called a default value for parameter platform. That
# means that unless specified otherwise, the argument for parameter platform
# will be set as 'playstation'.
# ln.49: on calling the function, we only had to input the value for argument
# name as we've already set a default value for platform.
# ln.50: on this call however, we've changed the argument for platform as
# 'gamecube', overriding the default value for platform which was
# 'playstation'.
