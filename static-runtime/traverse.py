import sys
import BeautifulSoup
import random
 
for i in range(10): 

    tree = BeautifulSoup.BeautifulSoup(open("tree.xml").read())

    score = 1

    prop_list = []
    for p in tree.findAll(name=["sex"]): prop_list.append(p['property'].encode())
    #print prop_list
    sex = random.sample(prop_list, 1)[0]
    sex_l = tree.findAll(name=["sex"], attrs={'property':sex})[0]
    score *= int(sex_l['value'])

    prop_list = []
    for p in sex_l.findAll(name=["mood"]): prop_list.append(p['property'].encode())
    #print prop_list
    mood = random.sample(prop_list, 1)[0]
    mood_l = sex_l.findAll(name=["mood"], attrs={'property':mood})[0]
    score *= int(mood_l['value'])
    
    prop_list = []
    for p in mood_l.findAll(name=["age"]): prop_list.append(p['property'].encode())
    #print prop_list
    age = random.sample(prop_list, 1)[0]
    age_l = mood_l.findAll(name=["age"], attrs={'property':age})[0]
    score *= float(age_l['value'])
    
    prop_list = []
    for p in age_l.findAll(name=["height"]): prop_list.append(p['property'].encode())
    #print prop_list
    ht = random.sample(prop_list, 1)[0]
    height_l = age_l.findAll(name=["height"], attrs={'property':ht})[0]
    score *= int(height_l['value'])
    
    prop_list = []
    for p in height_l.findAll(name=["weight"]): prop_list.append(p['property'].encode())
    #print prop_list
    wt = random.sample(prop_list, 1)[0]
    weight = height_l.findAll(name=["weight"], attrs={'property':wt})[0]
    score *= int(weight['value'])
    
    print "\n Sex :", sex, "Mood :", mood, "Age :", age, "Height :", ht, "Weight :", wt
    print "IQ Score : ", score/10.0
