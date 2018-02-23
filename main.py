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
    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("div#employee_div > table")

    if table:
        table_txt = table.text.strip().split("\n")
        try:
            position = table_txt[1].split(":")[1].strip()
        except:
            position = ""
        try:
            dept = table_txt[2].split(":")[1].strip()
        except:
            dept = ""
        try:
            building = table_txt[3].split(":")[1].strip()
        except:
            building = ""
        try:
            phone_num = table_txt[5].strip()
        except:
            phone_num
    else:
        position = ""
        dept = ""
        building = ""
        phone_num = ""

    print(position)
    print(dept)
    print(building)
    print(phone_num)
    return [position, dept, building, phone_num]

scraping(first_name="AHMAD", last_name="SAIYED")