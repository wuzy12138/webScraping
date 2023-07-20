#!/bin/python3
import urllib.request
from bs4 import BeautifulSoup

url = input('Enter - ')
html= urllib.request.urlopen(url).read() 
#.read() reads the whole blob with newlines at the end
# and it all comes into one big string
soup = BeautifulSoup(html, 'html.parser')

# find the "<a href = ... >"
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))