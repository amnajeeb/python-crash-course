# A dictionary in a dictionary, p.113

# In this exampled were're gonna have a dictionary of users, with usernames as
# keys, and "multiple lines of info as a dictionary" as values.

users = {
    'mj23': {
        'first': 'michael',
        'last': 'jordan',
        'location': 'chicago',
        },
    'lbj23': {
        'first': 'lebron',
        'last': 'james',
        'location': 'los angeles',
        }
    }

for username, user_info in users.items():
    print('Username: ' + username)
    full_name = user_info['first'].title() + ' ' + user_info['last'].title()
    print('\tFull name: ' + full_name)
    print('\tLocation: ' + user_info['location'].title())
