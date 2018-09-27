import requests
from bs4 import BeautifulSoup
from time import sleep # used to slow down scraping
from random import choice
from csv import DictWriter


BASE_URL = "http://quotes.toscrape.com" # CAPS used just to show that it is a constant


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        res = requests.get(f"{BASE_URL}{url}")
        # print(f"Now scraping {BASE_URL}{url}.....")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "bio_link": quote.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(1) # will slow down the scraping per loop by 1 seconds...
    return all_quotes

quotes = scrape_quotes()
# write quotes to a CSV file
def write_quotes(quotes):
    with open ("quotes.csv", "w", encoding='utf-8') as file:
        headers = ["text", "author", "bio_link"]
        csv_writer = DictWriter(file, fieldnames=headers, lineterminator= '\n')
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)