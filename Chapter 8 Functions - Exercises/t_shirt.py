# Exercises p.141.

# 8-3 + 8-4


def make_shirt(size, message='I love Python'):
    """Accepts size of t-shirt and message to be printed on it"""
    print("We've made your t-shirt size " + size.title() +
          ", and we've printed the following message on it: " +
          message.title() + ".")


make_shirt('m')
make_shirt('l')
make_shirt('l', 'I love New York')

print('\n')

# 8-5


def describe_city(city, country='japan'):
    """Describe cities and their countries"""
    print(city.title() + " is in " + country.title() + ".")


describe_city('tokyo')
describe_city('toronto', 'canada')
describe_city('osaka')
