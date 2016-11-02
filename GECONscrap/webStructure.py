from lxml import html
import requests
from bs4 import BeautifulSoup
url = "http://link.springer.com/chapter/10.1007/978-3-319-14609-6_4/fulltext.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
print(soup.prettify())