from album_labels import album_labels
from author_and_title import author_and_title
from credits import credits
from parse_songs import parse_songs
from versions_parser import parse_version
from soup_creator import create_soup
from database_facade import save_record


def parse_record(soup):
    album_dict = album_labels(soup)
    author, album_title = author_and_title(soup)
    credits_dict = credits(soup)
    song_titles, song_durations = parse_songs(soup)
    versions_dict = parse_version(soup)
    save_record(album_dict, author, album_title, credits_dict, song_titles, song_durations, versions_dict)
