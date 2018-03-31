import requests
from bs4 import BeautifulSoup


#max_pages = 26662

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.discogs.com/search/?type=master&page=2' + str(page) + '&country_exact=Serbia'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'search_result_title'}):
            global href
            href = "https://www.discogs.com" + link.get('href')
            print(href)
        page += 1
        

trade_spider(1)