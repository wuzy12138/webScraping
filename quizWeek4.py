#!/bin/python3
import re
import urllib.request
from bs4 import BeautifulSoup
# url = "http://py4e-data.dr-chuck.net/known_by_Sionan.html"
url = input('Enter - ')
html= urllib.request.urlopen(url).read() 
#.read() reads the whole blob with newlines at the end
# and it all comes into one big string


# find the "<tr>"

# total = 0
count = int(input('Enter count: '))
position = int(input("Enter position: "))
names = []
for i in range(count):
    print("Retrieving: {0}".format(url))
    html= urllib.request.urlopen(url).read() 
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[position-1].decode()
    name = re.findall(">(.+)<", tag)
    names.append(name)
    url = re.findall("href=\"(.+)\"", tag)[0]
    # print(tag)
    # y = re.findall(">([0-9]+)<", tag.decode())
    # y = 
    # htmlList.append(y)

print(names[-1])

    
