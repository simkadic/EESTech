from soup_creator import create_soup


def parse_version(href):
    soup = create_soup(href)
    id = soup.find('table', {'id': 'versions'})
    if id is not None:
        title = id.find('td', {'class': 'title'})
        album_name = title.find('a').text
        format = title.find('span', {'class': 'format'}).text
        country = id.find('td', {'class': 'country has_header'}).contents[0].text
        year = id.find('td', {'class': 'year has_header'}).text
        dict = {'album_name': album_name, 'format': format, 'country': country, 'year': year}
        
        print(dict)
        return dict

parse_version('https://www.discogs.com/Ansambel-Alojza-Grnjaka-Pri-Nas-Doma/release/9994716')
