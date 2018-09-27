import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get("https://www.rithmschool.com/blog")
# print(response.text) # to test response GET works...

soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
# print(articles)


with open("blog_data.csv", "w", encoding='utf-8') as csv_file:
    headers = ["title", "link", "date"]
    csv_writer = writer(csv_file, lineterminator= '\n')
    csv_writer.writerow(headers)
    for article in articles:
        # initial anchor tags
        a_tag = article.find("a")
        # find TITLE
        title = a_tag.get_text()
        # find HREF
        url = a_tag["href"]
        # find DATE
        date = article.find("time")["datetime"]
        # Test finds()
        # print(title, url, date)
        csv_writer.writerow([title, url, date])