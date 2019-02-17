# Exercises p.155

# 8-12


def make_sandwich(*items):
    """Creates a list of items to be included in a sandwich"""
    print("Here are the ingredients that you've selected for your sandwich:")
    for item in items:
        print("\t- " + item.title().strip())


make_sandwich('tomato', 'cucumber', 'mayonnaise', 'chicken')
make_sandwich('tuna', 'tomato sauce', 'prawn', 'cucumber')


# 8-13

def make_profile(first, last, **user_info):
    """Creates a profile that accepts user generated data and put it in a
    dictionary"""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


build_profile = make_profile('kobe', 'bryant', place_of_birth='Philadelphia',
                             team='los angeles lakers', draft_year=1996)
print(build_profile)


# 8-14


def build_car(manufacturer, model, **options):
    """Creates a profile for a car with user input for options stored in
    dictionary"""
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model
    for key, value in options.items():
        car_profile[key] = value
    return car_profile


make_car = build_car('nissan', 'gtr', year=2018, color='black')
print(make_car)


print("\nYou've picked a " + make_car['manufacturer'].title() + " " +
      make_car['model'].upper() + ", year " + str(make_car['year']) +
      ", color " + make_car['color'].title() + ".")
