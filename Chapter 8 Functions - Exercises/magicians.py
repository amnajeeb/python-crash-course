# Exercise p.150

# 8-9

players = ['hakeem olajuwon', 'kobe bryant', 'lebron james', 'john stockton']
great_players = []


def show_players(names):
    """prints names"""
    for name in names:
        print("All-Time Great: " + name.title() + "!")


show_players(players)


# 8-10

def make_great(names, great_names):
    """"""
    while names:
        name = names.pop()
        name = "The Great " + name.title() + "!"
        great_names.append(name)
        print(name)


make_great(players, great_players)
print(players)
print(great_players)
