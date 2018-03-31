
def album_labels(soup):
    keys=[]; vals=[]; dict={}
    for div in soup.find_all('div', {'class': 'head'}):
       keys.append(div.text)
    for div in soup.find_all('div', {'class': 'content'}):
       vals.append(div.text.replace('\n', '').strip())
    for i in range(len(keys)):
        dict[keys[i]] = vals[i]
    # TODO: razdvojiti stilove i/ili zanrove
    return dict
