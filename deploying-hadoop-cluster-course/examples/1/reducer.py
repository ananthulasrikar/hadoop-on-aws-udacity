#! /usr/bin/python

import sys

salesTotal = 0
oldkey = None

#Looping around the data
# It will be in the format key\t val
# Where key is the store name, val is the sale amount
#
# All the sales  for a particular store will be presented
# then the key will change and we will be dealing with next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        #Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesTotal
    
