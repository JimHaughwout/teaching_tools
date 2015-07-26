#!/usr/bin/python

import csv
import json
from sys import argv, exit
from random import uniform

# Let's build a list of random numbers
my_list = list()
for number in range(0,4):
    my_list.append(uniform(1,100))

print "List length is %d" % len(my_list)

print "List is %s" % my_list
print "Sorted list is %s" % sorted(my_list)
print "List sorted in reverse is %s" % sorted(my_list, reverse=True)
print "List elements are:"
for item in my_list:
    print "Index: %d, Item: %s" % (my_list.index(item), item)
