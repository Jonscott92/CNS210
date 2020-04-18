#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import urllib.request

url = 'https://www.python.org/downloads/'
page = requests.get(url)
# parse python.org/downloads for 2.7 version released on April 6, 2013
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
python_versions = soup.find(class_='list-row-container menu')
#print(python_versions)
correct_version = (python_versions.select("li:nth-of-type(66)"))
#print(correct_version)
# 2nd URl parse for the 2.7.4 Download Doc's page
url_2 = 'https://www.python.org/downloads/release/python-274/'
page_2 = requests.get(url_2)
souper = BeautifulSoup(page_2.content, 'html.parser')
python_download = souper.find('div', id='download')
#print(python_download)
correct_download = python_download.find('a', href="/ftp/python/2.7.4/Python-2.7.4.tar.xz")
print(correct_download)
dynamic = correct_download['href']
print(dynamic)
#Download to JonScott-Python-Version
print("Begin Download")
urllib.request.urlretrieve("https://www.python.org" + dynamic, "JonScott-python-version")
print('Download Complete!')