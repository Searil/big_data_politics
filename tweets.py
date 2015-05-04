#!/usr/bin/env python
import mincemeat



#-*- coding: utf-8 -*-
import locale
with open("tweets.txt","r") as ins:
    array = []
    for line in ins:
        line = unicode(line, 'UTF-8')
        line = line.replace("\n","")
        array.append(line)
array2 = []
for i in array:
    array2.append(i)

data = array2

with open("poz_neg.txt","r") as ins:
	poz_neg = []
	for line in ins:
		line = unicode(line, 'UTF-8')
		line = line.replace("\n","")
		poz_neg.append(line)
poz = 0
neg = 0

	

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))
def mapfn(k, v):
    for w in v.split():
	for p_n in poz_neg:
		if d == p_n:
			poz = poz + 1
		else: 
			neg = neg + 1
	yield poz,neg	

def mapfn(k, v):
    for w in v.split():
        yield w, 1

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="435123")
print results
