def vocals(soup):
    vocalists = []
    
    for span in soup.find_all('span', {'class': 'role'}):
        if str("Vocals").lower() in span.text.lower():
            parent = span.parent
            for vocallist in parent.find_all('a', {'class': 'rollover_link'}):
                vocalists.append(vocalist)
                
    return vocalists
