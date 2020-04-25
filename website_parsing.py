#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import urllib.request

url = 'https://www.python.org/downloads/'
page = requests.get(url)
# parse python.org/downloads for 2.7 version released on April 6, 2013
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
all_versions = soup.select('.download-list-widget .list-row-container li')
for version in all_versions:
    for x in version.select(".release-date"):
        if x.get_text() == "April 6, 2013":
           print(version.select_one('.release-number').get_text().split(" ")[1])
versions = input("which version of python would you like?")

selected_version ='https://www.python.org/ftp/python/' + versions +' /Python-' + versions + '.tar.bz2'
my_name_version = "JonScott-Python-version"
urllib.request.urlretrieve(selected_version, my_name_version)
