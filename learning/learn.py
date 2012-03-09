from math import log
import types

target = "Decision"
example = "Weekend"

def Entropy(T): # T is a Table
    size = float(len(T))
    hh = {}
    dec = []

    for row in T:
        dec.append(row[decision])

    for val in dec:
        if val in hh.keys():
            hh[val] += 1
        else:
            hh[val] = 1

    E = 0.0
    for val in hh.values():
        E += -(1*val/size) * log(val/size , 2) 
        
#    print "E : " , E
    return E


def Gain(T, attribute):
    value_set = set([])
    for t in T:
        value_set.add(t[attribute])
    
    gain = Entropy(T)
    for v in value_set:
        T_v = strip_table(T,attribute,v)
        gain = gain - ((len(T_v)*Entropy(T_v)) / len(T))
    return gain

def strip_table(T,attribute,value): #(attribute, value) on which to strip table T
    table_stripped = []
    for t in T:
        if t[attribute] == value:
            table_stripped.append(t)
    return table_stripped


def get_next_node(T):
    keys = T[0].keys()
    keys.remove(target)
    keys.remove(example)
    h = {}
    for attribute in keys:
        h[attribute] = Gain(T,attribute)
        print "Gain", attribute , ": ", h[attribute]
    print h
    next_node = max(h, key=h.get)
    return [next_node, h[next_node]] # return next_node and its Gain value


def learn(T):
    tree = {}
    
    print "\nLENGTH : ", len(T)
    for t in T:
        print t
    next_node = get_next_node(T)

    if next_node[1] == 0.0: #if Gain value is 0.0 then return a leaf
        return T[0][target]

    next_node = next_node[0]
        
    print "NEXT NODE : ", next_node
    value_set = set([])
    for t in T:
        value_set.add(t[next_node])

    for v in value_set:
        tree[(next_node, v)] = learn(strip_table(T, next_node, v))

    return tree


inputfile = raw_input("Input File --> ")
input = open(inputfile)
table = []

prop = input.readline().split()
decision = prop[len(prop)-1]
for l in input.readlines():
    table.append(dict(zip(prop,l.split())))
    
    
print table
Entropy(table)
print "dec : ", decision 

def print_hash(h,depth):
    depth += 1
    for k in h.keys():
        print '-'*depth, k
        if isinstance(h[k], types.DictType):
            print_hash(h[k], depth)
        else: print '-'*depth, '=>', h[k]

TREE = learn(table)
print "FINAL ", TREE


print_hash(TREE,0)
