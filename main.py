from urllib import *
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
import urllib.request
import requests
from io import BytesIO
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from lxml import html
from datetime import date, datetime, timedelta
from dateutil.relativedelta import *


def scraping(first_name="", last_name=""):

    url = "http://www.famu.edu/directory/employeesearch.cfm"
    url = url + "?srch={}+{}&submit=Search".format(first_name, last_name)

    r = requests.post(url)
    
    html = r.content.decode()

    print(html)


scraping(first_name="RANDALL", last_name="ABATE")