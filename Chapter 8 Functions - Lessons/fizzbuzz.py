for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3:
        print('Fizz')
    else:
        print(number)

# Important points.
# 1. List the requirements of the problem
# 2. Classify the requirements on the order that you want them to be sorted by
# Python. In the example above, you should prioritize the 2-condition
# requirement (number % 3 and number % 5) so that we ensure that the two other
# 1-condition requirements do not superceed the 2-condition requirements.
