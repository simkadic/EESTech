from bs4 import BeautifulSoup
import requests


def vocals(href):
    source_code = requests.get(href)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    
    for span in soup.find_all('span', {'class': 'role'}):
        if "Vocals" in span.text:
            vocals = soup.find('a', {'class': 'rollover_link'})
            children = vocals.findChildren()
            for child in children:
                print(child)
           # print(link.text)

 
vocals('https://www.discogs.com/Zdravko-Čolić-Kad-Pogledaš-Me-Preko-Ramena/release/6792758')
