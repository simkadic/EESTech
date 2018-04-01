def author_and_title(soup):
    ret = []
    for id in soup.findAll('h1', {'id': 'profile_title'}):
        title = str(id.text).strip().replace('\n', '').replace("'", "").split('\u200e–')
        for s in title:
            ret.append(s.strip())
        return ret
