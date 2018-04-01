def credits(soup):
    role = []; people = []; dict = {}
    for span in soup.find_all('span', {'class': 'role'}):
       role.append(span.text.replace("'", "\'"))
    for a in soup.find_all('a', {'class': 'rollover_link'}):
       people.append(a.text.replace('\n', '').replace("'", ""))
    for i in range(len(role)):
        dict[role[i]] = people[i]
    keys_for_deletion = []
    for key, value in dict.items():
        if not value:
            keys_for_deletion.append(key)
    for key in keys_for_deletion:
        del dict[key]
    #TODO:Split roles since one person has more than one role sometimes
    return dict
