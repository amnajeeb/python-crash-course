# Exercises p.121

# 7.1

car = input('What car brand would you like to rent? ')
print('Let me see if I can find you a ' + car.title() + '.')

# 7.2

dinner_group = int(input("How many people will attend the dinner? "))

if dinner_group > 8:
    print('You will have to wait for a table.')
else:
    print('We have a table available for you!')

# 7.3

number = int(input('What is your favorite number? '))

if (number % 10 == 0):
    print('Your number ' + str(number) + ' is a multiple of 10.')
else:
    print('Your number ' + str(number) + ' is not a multiple of 10.')
