def author_and_title(soup):
    for id in soup.findAll('h1', {'id': 'profile_title'}):
        title = str(id.text).strip().replace('\n', '').split('\u200e–')
        ret = []
        for s in title:
            ret.append(s.strip())
        return ret
