# If statements, starting ln.82

age = 19

if age >= 18:
    print('You are old enough to vote!')
    print('\nAre you registered to vote?')
    response = ' Yes  '
    response = response.lower().strip()
    if response == 'yes':
        print('\nWell done!')
else:
    print('You are not old enough to vote.')
    print('\nPlease register to vote when you reach the age of 18.')
