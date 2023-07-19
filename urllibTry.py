#!/bin/python3
# we have a library that does all the socket work for 
# us and makes web pages look like a file
import urllib.request

counts = dict()
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    words = (line.decode().strip())
    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
print("------------------------------------------\n")
print(counts)