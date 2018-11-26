guest_list = ['Steve Jobs', 'Kobe Bryant', 'Brian Cashman', 'Tom Hanks']
message0 = 'Hi ' + guest_list[0] + ', I\'d like to invite you to a dinner.'
message1 = 'Hi ' + guest_list[1] + ', I\'d like to invite you to a dinner.'
message2 = 'Hi ' + guest_list[2] + ', I\'d like to invite you to a dinner.'
message3 = 'Hi ' + guest_list[3] + ', I\'d like to invite you to a dinner.'
print(message0)
print(message1)
print(message2)
print(message3)

cant_make_it = 'Tom Hanks'
print(cant_make_it)

# remove guest with .remove() method

guest_list.remove(cant_make_it)

# add guest with .append() method

guest_list.append('Satoshi Nakamoto')
print(guest_list)

message0 = 'Hi ' + guest_list[0] + ', I\'d like to invite you to a dinner.'
message1 = 'Hi ' + guest_list[1] + ', I\'d like to invite you to a dinner.'
message2 = 'Hi ' + guest_list[2] + ', I\'d like to invite you to a dinner.'
message3 = 'Hi ' + guest_list[3] + ', I\'d like to invite you to a dinner.'
print(message0)
print(message1)
print(message2)
print(message3)
message0 = 'Hi ' + guest_list[0] + ', I\'ve found a bigger table.'
message1 = 'Hi ' + guest_list[1] + ', I\'ve found a bigger table.'
message2 = 'Hi ' + guest_list[2] + ', I\'ve found a bigger table.'
message3 = 'Hi ' + guest_list[3] + ', I\'ve found a bigger table.'
print(message0)
print(message1)
print(message2)
print(message3)

guest_list.insert(0, 'Elon Musk')
guest_list.insert(2, 'LeBron James')
guest_list.append('Nassim Taleb')
print(guest_list)

message0 = 'Hi ' + guest_list[0] + ', I\'d like to invite you to a dinner.'
message1 = 'Hi ' + guest_list[1] + ', I\'d like to invite you to a dinner.'
message2 = 'Hi ' + guest_list[2] + ', I\'d like to invite you to a dinner.'
message3 = 'Hi ' + guest_list[3] + ', I\'d like to invite you to a dinner.'
message4 = 'Hi ' + guest_list[4] + ', I\'d like to invite you to a dinner.'
message5 = 'Hi ' + guest_list[5] + ', I\'d like to invite you to a dinner.'
message6 = 'Hi ' + guest_list[6] + ', I\'d like to invite you to a dinner.'
print(message0)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)

message0 = 'Sorry ' + guest_list[0] + ', I can only invite 2 persons.'
message1 = 'Sorry ' + guest_list[1] + ', I can only invite 2 persons.'
message2 = 'Sorry ' + guest_list[2] + ', I can only invite 2 persons.'
message3 = 'Sorry ' + guest_list[3] + ', I can only invite 2 persons.'
message4 = 'Sorry ' + guest_list[4] + ', I can only invite 2 persons.'
message5 = 'Sorry ' + guest_list[5] + ', I can only invite 2 persons.'
message6 = 'Sorry ' + guest_list[6] + ', I can only invite 2 persons.'
print(message0)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)

guest_list.pop(0)
guest_list.pop(1)
guest_list.pop(2)
guest_list.pop(3)
guest_list.pop()
print(guest_list)

# When using .pop() method, one can only use an integer to specify item
# to be removed. To remove item based on value, see .remove() method

print('Hey '+guest_list[0]+', you\'re still invited to my dinner.')
print('Hey '+guest_list[1]+', you\'re still invited to my dinner.')

del guest_list[0]
del guest_list[0]
print(guest_list)
