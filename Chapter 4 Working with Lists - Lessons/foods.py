# Copying a list, p.67

my_foods = ['steak', 'chops', 'ribeye', 'broth']
friends_foods = my_foods[:]
print(friends_foods)

# Removes (not permanently) the fourth item in my_foods list, i.e. 'broth'.
my_foods.pop(3)

# Adds 'water' in list friends_foods.
friends_foods.append('water')

print("My favorite foods are:")
for item in my_foods:
    print(item.title())

print("My friend's favorite foods are:")
for item in friends_foods:
    print(item.title())

# IMPORTANT NOTE: If we set that friends_foods = my_foods (WITHOUT DUPLICATING
# LIST by using the brackets), the list will be linked and any change to one
# list will affect the other.
