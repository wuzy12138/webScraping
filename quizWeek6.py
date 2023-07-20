#!/bin/python3
# 1. load url and store html into a string
# 2. parse json with json.loads() into a dictionary
# 3. use dictionary access to find the things we want
# 4. Process stats

import urllib.request
import json

url = input("Enter Location: ")
print("Retrieving", url)

html= urllib.request.urlopen(url).read()

info = json.loads(html)
# tree.find('name').text
print("Retrieved", len(html), "characters")
comments = info["comments"]
# counts = tree.findall(".//count")
inc = 0
totalSum = 0
for comment in comments:
    totalSum += (comment["count"])
    inc += 1

print("Count:", inc)
print("Sum:", totalSum)
# print("Count:", len(counts))

