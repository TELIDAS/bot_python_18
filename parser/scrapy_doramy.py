# pip install requests
# pip install bs4
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0"
}
URL = "https://doramy.club/genre/fentezi"


def get_requests(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="post-home")
    shows = []

    for item in items:
        shows.append(
            {
                "link": item.find("a").get("href"),
                "title": item.find("a").find("span").get_text(),
                "img": item.find("a").find("img").get("src"),
            }
        )
    return shows


def scrapy_script():
    html = get_requests(URL)
    if html.status_code == 200:
        shows = []
        for page in range(1, 71):
            html = get_requests(f"https://doramy.club/genre/fentezi/page/{page}")
            shows.extend(get_data(html.text))
        return shows
    else:
        raise Exception("Error in scrapy script function")
