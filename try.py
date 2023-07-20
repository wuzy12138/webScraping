#!/bin/python3
import re

# info = "<p>Please click <a href=\"http://www.dr-chuck.com\">here</a></p>"
# info = "<tr><td>Modu</td><td><span class=\"comments\">90</span></td></tr>"
info = "<a href=\"http://py4e-data.dr-chuck.net/known_by_Abdallah.html\">Abdallah</a>"
# use () to choose the content to be regEx
# y = re.findall("href=\"(.+)\"", info)
y = re.findall(">(.+)<", info)
print(y)