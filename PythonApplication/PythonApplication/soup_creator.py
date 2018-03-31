from bs4 import BeautifulSoup
import requests


def create_soup(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    return BeautifulSoup(plain_text, "html.parser")
