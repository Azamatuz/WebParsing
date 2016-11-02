#import sys
#import re
#from lxml import html
import requests
from bs4 import BeautifulSoup

r = requests.get("http://link.springer.com/chapter/10.1007/978-3-319-14609-6_1/fulltext.html")
soup = BeautifulSoup(r.content, "lxml")
vol= str(soup.find('span', {'class': 'vol-info'}).text.replace('of the series Lecture Notes in Computer Science', ''))
print("GECON, Intl Conf on Grids, Clouds, Systems, and Services. LNCS, "
                       + vol.strip() + ', '
                       + str(soup.find('span', {'class': 'page-numbers-info'}).text) + ', ' + "Springer, 2014.")