from soup_creator import create_soup


def vocals(href):
    soup = create_soup(href)
    
    for span in soup.find_all('span', {'class': 'role'}):
        if str("Vocals").lower() in span.text.lower():
            parent = span.parent
            for vocallist in parent.find_all('a', {'class': 'rollover_link'}):
                print(vocallist.text)

 
vocals('https://www.discogs.com/Nikolija-101-Propušteni-Poziv/release/9843081')
