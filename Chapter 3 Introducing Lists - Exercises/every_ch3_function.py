# Functions studied in chapter 3:
# FUNCTIONS
# sorted() ln.43
# len() ln.

# METHODS
# .append() ln. 17
# .insert() ln. 21
# .pop() ln. 25
# .remove() ln. 29
# .sort() ln. 41

# STATEMENTS
# del ln. 36

places = ['namibia', 'kamchatka', 'sapporo', 'cambodia', 'rwanda']
print("Here\'s a list of places I\'d like to see:\n")
print(places)

places.append('taiwan')
print("\nHere\'s an updated list of places I\'d like to visit:\n")
print(places)

places.insert(2, 'cape town')
print("\nHere\'s an updated list of places I\'d like to visit:\n")
print(places)

places.pop(3)
print("\nIf I had to pick 5 places to visit, that\'d be the following:\n")
print(places)

places.remove('cape town')
print("\nIf I had to pick 4 places to visit, that\'d be the following:\n")
print(places)

del places[3]
del places[2]
print("\nMy final 3 picks for places I\'d love to visit:\n")
print(places)

places.sort(reverse=True)
print(places)
print(sorted(places, reverse=False))

print("\nNumber of places I\'d love to visit:\n")
print(len(places))
