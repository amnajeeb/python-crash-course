# Exercise p.159

# 8-16


def show_players(names):
    """prints names"""
    for name in names:
        print("All-Time Great: " + name.title() + "!")


def make_great(names, great_names):
    """"""
    while names:
        name = names.pop()
        name = "The Great " + name.title() + "!"
        great_names.append(name)
        print(name)
