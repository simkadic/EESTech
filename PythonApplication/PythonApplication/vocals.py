from bs4 import BeautifulSoup
import requests


def vocals(href):
    source_code = requests.get(href)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    
    for span in soup.find_all('span', {'class': 'role'}):
        if str("Vocals").lower() in span.text.lower():
            parent = span.parent
            for vocallist in parent.find_all('a', {'class': 'rollover_link'}):
                print(vocallist.text)

 
vocals('https://www.discogs.com/Nikolija-101-Propušteni-Poziv/release/9843081')
