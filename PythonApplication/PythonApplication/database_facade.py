from database import add_credits_to_album, add_song, connect_album_to_author, connect_album_to_genre, connect_album_to_style, connect_album_to_style, connect_version_to_format, insert_album, insert_author, insert_country, insert_format, insert_genre, insert_role, insert_style, insert_version
import util

def save_record(album_dict, author, album_title, credits, song_titles, song_durations, versions_dict):
    insert_album.func(album_title)
    insert_author.func(author)
    try:
        insert_format.func(album_dict['Format'])
    except:
        pass
    try:
        insert_style.func(album_dict['Style'])
    except:
        pass
    try:
        insert_genre.func(album_dict['Genre'])
    except:
        pass
    for key, value in credits.items():
        insert_role.func(key)
        add_credits_to_album.func(album_title, value, key)
    try:
        insert_country.func(album_dict['Country'])
    except:
        pass
    connect_album_to_author.func(album_title, author)
    try:
        connect_album_to_style.func(album_title, album_dict['Style'])
    except:
        pass
    try:
        connect_album_to_genre.func(album_title, album_dict['Genre'])
    except:
        pass
    try:
        transformed_date = util.transform_date(album_dict['Released'])
    except:
        pass
    try:
        insert_version.func(album_title, album_dict['Country'], transformed_date[0], transformed_date[1], transformed_date[2])
    except: 
        pass
    try: 
        connect_version_to_format.func(album_title, album_dict['Country'], transformed_date[0], transformed_date[1], transformed_date[2], album_dict['Format'])
    except: 
        pass
    for i in range(len(song_titles)):
        if song_durations[i]:
            minutes, seconds = song_durations[i].split(':')
        else:
            minutes, seconds = '', ''
        add_song.func(album_title, song_titles[i], minutes, seconds)
    if versions_dict['Year']:
        insert_version.func(album_title, versions_dict['Country'], 1, 1, versions_dict['Year'])
        connect_version_to_format.func(album_title, versions_dict['Country'], 1, 1, versions_dict['Year'], album_dict['Format'])
