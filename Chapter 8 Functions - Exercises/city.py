# Exercises p.146

# 8-6


def city_country(city_name, country_name):
    """Takes a name of a city and its country and formates them."""
    city_country_combo = city_name + ', ' + country_name
    return city_country_combo.title()


city0 = city_country('new york', 'united states')
city1 = city_country('tokyo', 'japan')
city2 = city_country('windhoek', 'namibia')

print(city0)
print(city1)
print(city2)

# 8.7


def make_album(artist_name, album_title, track_number=''):
    """Creates a dictionary for music album."""
    album = {'artist': artist_name,
             'album title': album_title,
             }
    if track_number:
        album['track number'] = track_number
    return album


hiphop_album = make_album('nas', 'illmatic', 11)
electro_album = make_album('air', 'moon safari')
rap_album = make_album('dr dre', 'chronic 2001', 21)
print(hiphop_album)
print(electro_album)
print(rap_album)


# 8-8

def make_album1(artist_name, album_title, track_number=''):
    """Creates a dictionary for music album."""
    album = {'artist': artist_name,
             'album title': album_title,
             }
    if track_number:
        album['track number'] = track_number
    return album


artist_input = "Who's your favorite artist? "
album_input = "What's your favorite album of his/hers? "

while True:
    print("Type 'quit' to leave the program")
    artist = input(artist_input)
    if artist == 'quit':
        break
    album = input(album_input)
    if album == 'quit':
        break

    album_artist = make_album1(artist, album)
    print(album_artist)


# ln.53/54: To better organise the code, we can prepare the prompt message and
# include them in variables, that we then use in lines 58 and 61.
