from soup_creator import create_soup


def authorAndTitle(href):
    soup = create_soup(href)
    for id in soup.findAll('h1', {'id': 'profile_title'}):
        title = str(id.text).strip().replace('\n', '').split('\u200e–')
        ret = []
        for s in title:
            ret.append(s.strip())
        return ret

authorAndTitle('https://www.discogs.com/Nikolija-101-Propušteni-Poziv/release/9843081')
