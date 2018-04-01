def parse_songs(soup):
    titles = []
    durations = []

    for link in soup.find_all('span', {'class': 'tracklist_track_title'}):
        titles.append(link.text.replace("'", ""))

    for link in soup.find_all('td', {'class': 'tracklist_track_duration'}):
        cleared_string = link.text.replace('\n', '')
        cleared_string = cleared_string.replace("'", "")
        if not cleared_string:
            cleared_string = '0:0'
        durations.append(cleared_string)

    return titles, durations
