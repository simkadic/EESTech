from soup_creator import create_soup


def author(href):
    soup = create_soup(href)
    for id in soup.findAll('h1', {'id': 'profile_title'}):
        #print(id.text)
        for span in id.find_all('a'):
            print(span.text)

author('https://www.discogs.com/Nikolija-101-Propušteni-Poziv/release/9843081')
