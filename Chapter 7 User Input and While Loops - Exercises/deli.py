# Exercise p.131

# 7-8

sandwich_orders0 = ['tuna', 'hamburger', 'cheeseburger', 'doner', 'panini']

finished_sandwiches = []

while sandwich_orders0:  # i.e. while there are items in sandwich_orders
    ordered_sandwich = sandwich_orders0.pop()
    print("Your " + ordered_sandwich.title() + " is ready!")
    finished_sandwiches.append(ordered_sandwich)

print("\nList of sandwiches made today:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich.title())

# 7-9

sandwich_orders1 = ['tuna', 'pastrami', 'hamburger', 'cheeseburger',
                    'pastrami', 'doner', 'panini', 'pastrami']

finished_sandwiches1 = []


print('\nPlease be aware that we\'ve run out of pastramis.')

while 'pastrami' in sandwich_orders1:
    sandwich_orders1.remove('pastrami')

while sandwich_orders1:  # i.e. while there are items in sandwich_orders
    ordered_sandwich = sandwich_orders1.pop()
    print("Your " + ordered_sandwich.title() + " is ready!")
    finished_sandwiches1.append(ordered_sandwich)

print("\nList of sandwiches made today:")
for sandwich in finished_sandwiches1:
    print("\t" + sandwich.title())


# 7-10

poll = {}

poll_status = True

while poll_status:
    name = input("What is your name? ")
    places = input("Which country would you like to visit? ")
    poll[name] = places

    repeat = input("Would you like to let a friend answer the poll? (yes/no) ")
    if repeat.strip().lower() == 'no':
        poll_status = False

for name, place in poll.items():
    print(name.title() + ' would like to visit ' + place.title() + ".")
