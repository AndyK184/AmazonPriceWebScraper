import requests
import subprocess
import time
from bs4 import BeautifulSoup

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15'}

URLs = ["Your_first_amazon_link_here",
        "Your_second_amazon_link_here"]


def findPrice(URLs):
    for tempURL in URLs:
        page = requests.get(tempURL, headers=headers)
        soup = BeautifulSoup(page.content, features="lxml")
        title = soup.select("#productTitle")[0].get_text().strip()
        price = soup.select("#priceblock_ourprice")[0].get_text().strip()
        converted_price = price[0:6].replace(",", ".")
        # die [:30] sind drin damit nicht die unnützen Zusätze ausgelesen werden
        p = subprocess.Popen(['say', title[:30] + 'kostet' + price])
        p.wait()


findPrice(URLs)
