# Chapter 3 exercise, p.50

places = ['namibia', 'kamchatka', 'sapporo', 'cambodia', 'rwanda']
print(places)

print(sorted(places))
print(places)

print(sorted(places, reverse=True))

# Note above argument FOLLOWS the list. There must be a white space after the
# comma.

print(places)

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)
places.sort(reverse=True)
print(places)

################################################
################################################

guest_list = ['Steve Jobs', 'Kobe Bryant', 'Brian Cashman', 'Tom Hanks']
print('Number of people attending the dinner: ')
print(len(guest_list))
