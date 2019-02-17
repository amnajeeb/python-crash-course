# Using Arbitrary keywords arguments p.153.


def build_profile(first, last, **user_info):
    """Creates a profile in a dictionary with information provided by user"""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('lebron', 'james', city='los angeles',
                             team='lakers', previous_team='cavaliers',
                             draft_year=2003)
print(user_profile)

# lanes 11 & 14: REMINDER that when using return, we need to specify a
# variable/list/dictionary or dictionary to store the data. The
# variable/list/dictionary specified ln.11 is only for the purpose of the
# function definition.
