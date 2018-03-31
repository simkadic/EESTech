from soup_creator import create_soup


def trade_spider():
    start_url = 'https://www.discogs.com/search/?type=release&limit=250&country_exact=Serbia'
    page = start_url + '&page=1'
    while page is not None:
        soup = create_soup(page)
        print('linkovi na jednoj strani:')
        for link in soup.findAll('a', {'class': 'search_result_title'}):
            href = "https://www.discogs.com" + link.get('href')
            print(href)
        print(page)
        page = get_next_page_with_delay(page)


trade_spider()
