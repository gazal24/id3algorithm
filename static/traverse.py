import sys
import BeautifulSoup

tree = BeautifulSoup.BeautifulSoup(open("tree.xml").read())

score = 1

for p in tree.findAll(name=["sex"]): print p['property']
sex = raw_input("sex> ")
sex_l = tree.findAll(name=["sex"], attrs={'property':sex})[0]
score *= int(sex_l['value'])


for p in sex_l.findAll(name=["mood"]): print p['property']
mood = raw_input("mood> ")
mood_l = sex_l.findAll(name=["mood"], attrs={'property':mood})[0]
score *= int(mood_l['value'])


for p in mood_l.findAll(name=["age"]): print p['property']
age = raw_input("age> ")
age_l = mood_l.findAll(name=["age"], attrs={'property':age})[0]
score *= float(age_l['value'])


for p in age_l.findAll(name=["height"]): print p['property']
ht = raw_input("height> ")
height_l = age_l.findAll(name=["height"], attrs={'property':ht})[0]
score *= int(height_l['value'])


for p in height_l.findAll(name=["weight"]): print p['property']
wt = raw_input("wieght> ")
weight = height_l.findAll(name=["weight"], attrs={'property':wt})[0]
score *= int(weight['value'])

print "\nIQ Score : ", score/10.0
