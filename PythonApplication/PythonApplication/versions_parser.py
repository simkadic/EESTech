def parse_version(soup):
    id = soup.find('table', {'id': 'versions'})
    dict = {'Album_name': '', 'Format': '', 'Country': '', 'Year': ''}
    if id is not None:
        title = id.find('td', {'class': 'title'})
        album_name = title.find('a').text
        format = title.find('span', {'class': 'format'}).text
        country = id.find('td', {'class': 'country has_header'}).contents[0].text
        year = id.find('td', {'class': 'year has_header'}).text
        dict = {'Album_name': album_name, 'Format': format, 'Country': country, 'Year': year}
    
    return dict
