from soup_creator import create_soup
from get_next_page import get_next_page_with_delay
from parse_record import parse_record
import database

def trade_spider(country = "Serbia"):
    start_url = 'https://www.discogs.com/search/?type=release&limit=250&country_exact=' + country
    start_url += '&type=release'
    page = start_url + '&page=1'
    conn = database.connect_to_db.connect()
    while page is not None:
        soup = create_soup(page)
        print('linkovi na jednoj strani:')
        for link in soup.findAll('a', {'class': 'search_result_title'}):
            href = "https://www.discogs.com" + link.get('href')
            print(href)
            try:
                parse_record(create_soup(href), conn)
            except KeyboardInterrupt:
                database.connect_to_db.disconnect(conn)
                break
        print(page)
        page = get_next_page_with_delay(page)
    database.connect_to_db.disconnect(conn)

trade_spider('Montenegro')
