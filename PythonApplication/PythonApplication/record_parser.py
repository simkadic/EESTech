from album_labels import album_labels
from author_and_title import author_and_title
from credits import credits
from parse_songs import parse_songs
from versions_parser import parse_version
from soup_creator import create_soup

def record_parser(soup):
    album_dict = album_labels(soup)
    author, title = author_and_title(soup)
    credits_dict = credits(soup)
    song_titles, song_durations = parse_songs(soup)
    versions_dict = parse_version(soup)
    print('album dict: ' + str(album_dict))
    print('author: ' + str(author))
    print('credits: ' + str(credits_dict))
    print('song titles: ' + str(song_titles))
    print('song durations: ' + str(song_durations))
    print('versions: ' + str(versions_dict))


soup = create_soup('https://www.discogs.com/Ansambel-Alojza-Grnjaka-Pri-Nas-Doma/release/11790302')
record_parser(soup)