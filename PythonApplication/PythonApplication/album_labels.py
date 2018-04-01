def album_labels(soup):
    keys = []
    vals = []
    dict = {}
    for div in soup.find_all('div', {'class': 'head'}):
        keys.append(div.text[:-1].replace("'", "\'"))
    for div in soup.find_all('div', {'class': 'content'}):
        vals.append(div.text.replace('\n', '').replace("'", "").strip())
    for i in range(len(keys)):
        dict[keys[i]] = vals[i]
    keys_for_deletion = []
    for key, value in dict.items():
        if not value:
            keys_for_deletion.append(key)
    for key in keys_for_deletion:
        del dict[key]
    
    # TODO: razdvojiti stilove i/ili zanrove
    return dict
