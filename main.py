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


def scraping(last_name="", first_name=""):

    url = "http://www.famu.edu/directory/employeesearch.cfm"
    