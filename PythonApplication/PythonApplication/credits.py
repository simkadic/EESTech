from soup_creator import create_soup


def credits(href):
    soup = create_soup(href)
    role = []; people = []; dict = {}
    for span in soup.find_all('span', {'class': 'role'}):
       role.append(span.text)
    for a in soup.find_all('a', {'class': 'rollover_link'}):
       people.append(a.text.replace('\n', ''))
    for i in range(len(role)):
        dict[role[i]] = people[i]
#TODO:Split roles since one person has more than one role sometimes 
    return dict
