from database import add_credits_to_album, add_song, connect_album_to_author, connect_album_to_genre, connect_album_to_style, connect_album_to_style, connect_version_to_format, insert_album, insert_author, insert_country, insert_format, insert_genre, insert_role, insert_style, insert_version


def save_record(album_dict, author, album_title, credits, song_titles, song_durations, versions_dict):
    insert_album.func(album_title)
    insert_author.func(author)
    insert_format.func(album_dict['Format'])
    insert_style.func(album_dict['Style'])
    insert_genre.func(album_dict['Genre'])
    for key, value in credits.items():
        insert_role.func(key)
        add_credits_to_album.func(album_title, value, key)
    insert_country.func(versions_dict['country'])
    connect_album_to_author.func(album_title, author)
    connect_album_to_style.func(album_title, album_dict['Style'])
    connect_album_to_genre.func(album_title, album_dict['Genre'])
    insert_version.func(album_title, versions_dict['country'], 1, 1, versions_dict['year'])
    connect_version_to_format.func(versions_dict['country'], 1, 1, versions_dict['year'], album_dict['Format'])
    for i in range(len(song_titles)):
        if song_durations[i]:
            minutes, seconds = song_durations[i].split(':')
        else:
            minutes, seconds = '', ''
        add_song.func(album_title, song_titles[i], minutes, seconds)
