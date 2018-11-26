# Start of Chapter 3 'Introducing lists', p.37

bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles)

print(bicycles[0].title())
print(bicycles[2].upper())
print(bicycles[3].upper())

message = 'My favorite bicycle is the '
print(message+bicycles[0].title()+'.')
message1 = message+bicycles[0].title()+'.'
print(message1)
