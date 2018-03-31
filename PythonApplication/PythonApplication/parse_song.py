from soup_creator import create_soup


def parse_link(href):
    soup = create_soup(href)
    titles = []
    durations = []

    for link in soup.find_all('span', {'class': 'tracklist_track_title'}):
        titles.append(link.text)

    for link in soup.find_all('td', {'class': 'tracklist_track_duration'}):
        durations.append(link.text.replace('\n', ''))

    return titles, durations


if __name__ == '__main__':
    titles, durations = parse_link('https://www.discogs.com/Faul-Deep-Thoughts-EP/release/4560348')
    print(titles, durations)
    titles, durations = parse_link('https://www.discogs.com/Bones-Beeker-Inside-a-Different-Mind/release/11786886')
    print(titles, durations)
