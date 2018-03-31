from bs4 import BeautifulSoup
import requests


def vocals(href):
    source_code = requests.get(href)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    
    for span in soup.find_all('span', {'class': 'role'}):
        if "Vocals" in span.text:
            parent = span.parent
            for vocallist in parent.find_all('a', {'class': 'rollover_link'}):
                print(vocallist.text)

 
vocals('https://www.discogs.com/Zdravko-Čolić-Kad-Pogledaš-Me-Preko-Ramena/release/6792758')
