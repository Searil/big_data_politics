#!/usr/bin/env python
import mincemeat

data = ["Humpty Dumpty sat on a wall",
        "Humpty Dumpty had a great fall",
        "All the King's horses and all the King's men",
        "Couldn't put Humpty together again",
        ]

#-*- coding: utf-8 -*-
import locale
with open("t22.txt","r") as ins:
    array = []
    for line in ins:
        line = unicode(line, 'UTF-8')
        line = line.replace("\n","")
        array.append(line)
array2 = []
for i in array:
    array2.append(i)

data = array2
# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

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

results = s.run_server(password="changeme")
print results
