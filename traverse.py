import urllib2
import re
import sys
import os
import string
import mechanize
import BeautifulSoup

tree = BeautifulSoup.BeautifulSoup(open("tree.xml").read())


sex = raw_input("sex> ")
mood = raw_input("mood> ")
age = raw_input("age> "))
ht = raw_input("height> "))
wt = raw_input("wieght> "))

score = 1

level = tree.findAll(name=["sex"], attrs={'property':sex})[0]
score *= int(level['value'])

level = level.findAll(name=["mood"], attrs={'property':mood})[0]
score *= int(level['value'])

level = level.findAll(name=["age"], attrs={'property':age})[0]
score *= int(level['value'])

level = level.findAll(name=["height"], attrs={'property':ht})[0]
score *= int(level['value'])

level = level.findAll(name=["weight"], attrs={'property':wt})[0]
score *= int(level['value'])

print score
