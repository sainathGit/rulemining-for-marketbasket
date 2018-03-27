
import sys

min_support = float(sys.argv[2])
min_confidence = float(sys.argv[4])

db = [];
tf = open(sys.argv[5], "r")

for line in tf:
    db.append([int(x) for x in line.split()])

min_support = min_support*len(db)




def clear(table):
    ktd = []
    for k in table.keys():
        if table[k] < min_support:
            ktd.append(k)

    for i in ktd:
        del table[i]

def get_key(l1, l2):
    key = []
    last = len(l1) - 1;
    for i in range(last):
        key.append(l1[i])

    key.append(l1[last])
    key.append(l2[last])   

    return tuple(key)

def can_mix(l1, l2):

    last = len(l1) - 1
    for i in range(last):
        if l1[i] != l2[i]:
            return False

    if l1[last] >= l2[last]:
        return False
    return True 


def apriori_gen(table):

    new_table = {}
    for l1 in table.keys():
        for l2 in table.keys():

            if can_mix(l1,l2):
                new_table[get_key(l1,l2)] = 0;
    
    return new_table



def count_values(table):
    
    for k in table.keys():
        for t in db:
            if set(k).issubset(set(t)):
                table[k] += 1


def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item


def print_rule(s, l_s, conf):

        print(s,end = " ==> ")
        print(l_s, end = "              " )
        print(conf)


def print_confs(item, L):
    
    global count
    for s in powerset(list(item)):
        if s == [] or s == list(item):
            continue
        l_s = [x for x in item if x not in s]
        conf = L[item]/L[tuple(s)]
        if  conf > min_confidence:
            print_rule(s,l_s,conf)
            count += 1



l = []
table = {}
for t in db:
    for x in t:
        if (x,) not in table.keys():
            table[(x,)] = 1
        else:
            table[(x,)] += 1


clear(table)
l.append(table)



#from here the main driver starts

k = 1
while (len(l[k-1]) != 0) :
   
    table = apriori_gen(l[k-1])
    count_values(table)
    clear(table)


    l.append(table)
    k += 1

l.pop()

L = {}
for k in range(len(l)):
    L.update(l[k])

count = 0
for item in L.keys():
    if len(item) > 1:
         print_confs(item,L) 

print("mined file ", sys.argv[5])
print("and found a total of ",count,"  association rules")

