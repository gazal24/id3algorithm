import sys
import BeautifulSoup

bad_v = 2.0
decent_v = 4.0
good_v = 6.0


young_v = 2.0
adolescent_v = 4.0
adult_v = 6.0


def sex_value(sex):
    if sex == "male":
        return 6
    elif sex == "female":
        return 4

def mood_value(mood):
    bad = decent = good = 0
    mood = float(mood)
    if mood <= 2:
        bad = 100
        decent = 0
        good = 0
        
    elif mood <= 4:
        bad = (5 - mood)*100.0/3
        decent = (mood - 2)*100.0/3
        good = 0

    elif mood <= 6:
        bad = 0
        decent = 100.0
        good = 0

    elif mood <= 8:
        bad = 0
        decent = (9 - mood)*100.0/3
        good = (mood - 6)*100.0/3

    elif mood <= 10:
        bad = 0
        decent = 0
        good = 100.0

#    print bad, decent, good
    return bad*bad_v + decent*decent_v + good*good_v


def age_value(age):
    young = adolescent = adult = 0
    age = float(age)
    if age <= 10:
        young = 100.0
        adolescent = 0
        adult = 0
        
    elif age <= 15:
        young = (15 - age)*100.0/5
        adolescent = (age - 10)*100.0/5
        adult = 0

    elif age <= 25:
        young = 0
        adolescent = 100.0
        adult = 0

    elif age <= 35:
        young = 0
        adolescent = (35 - age)*100.0/10
        adult = (age - 25)*100.0/10

    else:
        young = 0
        adolescent = 0
        adult = 100.0

#    print "age: ", young, adolescent, adult
    return young*young_v + adolescent*adolescent_v + adult*adult_v


sex = raw_input("sex> ")
sex_value(sex)

mood = raw_input("mood (1-10)> ")
mood_percent = mood_value(mood)

age = raw_input("age (1-100)> ")
age_percent = age_value(age)

tree = BeautifulSoup.BeautifulSoup(open("fuzzy_tree.xml").read())
score = 1

if(mood_percent < 300):
    mood_prop = "200"
elif (mood_percent < 500):
    mood_prop = "400"
else:
    mood_prop = "600"


if(age_percent < 300):
    age_prop = "200"
elif (age_percent < 500):
    age_prop = "400"
else:
    age_prop = "600"

age_l = tree.findAll(name=["age"], attrs={'property':age_prop})[0]
score *= int(age_l['value']) * age_percent
#print "score : ", score

mood_l = age_l.findAll(name=["mood"], attrs={'property':mood_prop})[0]
score *= float(mood_l['value']) * mood_percent
print "Final IQ : ", score/1000



