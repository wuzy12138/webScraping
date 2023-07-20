#!/bin/python3
# 1. load url and store html into a string
# 2. parse xml with xml.etree.ElementTree into a tree
# 3. use tree.findall to find the things we want
# 4. Process stats

import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter Location: ")
print("Retrieving", url)

html= urllib.request.urlopen(url).read()

tree = ET.fromstring(html)
# tree.find('name').text
print("Retrieved", len(html), "characters")

counts = tree.findall(".//count")
inc = 0
totalSum = 0
for count in counts:
    totalSum += int(count.text)
    inc += 1

print("Count:", inc)
print("Sum:", totalSum)
# print("Count:", len(counts))

