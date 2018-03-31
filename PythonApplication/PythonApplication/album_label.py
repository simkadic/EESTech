from soup_creator import create_soup


def album_labels(href):
    soup = create_soup(href)
    keys=[]; vals=[]; dict={}
    for div in soup.find_all('div', {'class': 'head'}):
       keys.append(div.text)
    for div in soup.find_all('div', {'class': 'content'}):
       vals.append(div.text.replace('\n', ''))
    for i in range(len(keys)):
        dict[keys[i]] = vals[i]
    # TODO: razdvojiti stilove i/ili zanrove
    return dict
