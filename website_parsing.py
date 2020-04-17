#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/downloads/'
page = requests.get(url)
# parse python.org/downloads for 2.7 version released on April 6, 2013
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.prettify())
python_versions = soup.find(class_='list-row-container menu')
#print(python_versions)
correct_version = (python_versions.select("li:nth-of-type(66)"))
print(correct_version)

# Download to JonScott-Python-Version
print('Download Starting')
download_link = 'https://www.python.org/ftp/python/2.4.7/Python-2.4.7.tgz'
r = requests.get(download_link)
with open("JonScott-Python-Version", "w") as f:
    f.write(str(r.content))
print('Download Complete!')