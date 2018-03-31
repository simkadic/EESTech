from soup_creator import create_soup


DELAY_CONSTANTS = [1, 6, 3, 3, 6, 12, 8]


def get_next_page(url):
    time.sleep(1)
    soup = create_soup(url)
    link = soup.find('a', {'class': 'pagination_next'})
    if link is None:
        return None
    href = link.get('href')
    return "https://www.discogs.com" + href


def get_next_page_with_delay(url):
    for i in range(0, len(DELAY_CONSTANTS)):
        href = get_next_page(url)
        if href is None:
            delay = 5 * DELAY_CONSTANTS[i]
            print('trying with delay(seconds): ' + str(delay))
            time.sleep(delay)
        else:
            return href
    return get_next_page(url)
