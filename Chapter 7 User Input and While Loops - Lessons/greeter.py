name = input('Please enter your name: ')
print('Hello, ' + name.title() + '!')

prompt = 'If you tell us who you are, we can personalise messages you see.'
prompt += '\nWhat is your name? '  # operator += adds another string to prompt.

name = input(prompt)
print('Hello, ' + name.title() + '!')
