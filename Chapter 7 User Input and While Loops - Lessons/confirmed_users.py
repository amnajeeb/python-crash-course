# Moving items from one list to another, p.128

# Starts with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['mariano', 'roy', 'mike', 'edgar']
confirmed_users = []

# Verified each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users

# Code below: while loop is used to go through the process of moving people
# from unconfirmed list to confirmed list UNTIL the unconfirmed_user list is
# empty.
# ln.19: "while unconfirmed_users has items in it..."
# ln.20: current_user is a user removed (hence .pop() method) from unconfirmed
# list.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print('Verifying user: ' + current_user.title() + '...')
    confirmed_users.append(current_user)

# Display all confirmed users

print('\nThe following users have been confirmed:')
for user in confirmed_users:
    print('\t' + user.title())

# REMINDER: to print each individual item in a list, use a for loop. If you try
# to print the list directly, it will print the list, i.e. with [] and ''.
