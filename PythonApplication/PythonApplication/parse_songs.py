def parse_songs(soup):
    titles = []
    durations = []

    for link in soup.find_all('span', {'class': 'tracklist_track_title'}):
        titles.append(link.text)

    for link in soup.find_all('td', {'class': 'tracklist_track_duration'}):
        durations.append(link.text.replace('\n', ''))

    return titles, durations
