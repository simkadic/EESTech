from album_label import album_label
from author_and_title import author_and_title
from credits import credits
from parse_songs import parse_songs
from versions_parser import parse_version

def record_parser(href):
    album_dict = album_label(href)
    author, title = author_and_title(href)
    credits_dict = credits(href)
    songs_list = parse_songs(href)
    versions_dict = parse_version(href)
    print(album_dict, author, credits_dict, songs_list, versions_dict)


record_parser('https://www.discogs.com/Ansambel-Alojza-Grnjaka-Pri-Nas-Doma/release/11790302')