#!/usr/bin/python

import csv
import json
from sys import argv, exit

if len(argv) != 2:
    print "Usage: %s source_file" % argv[0]
    exit(2)

source_file = argv[1]

with open(source_file) as csvfile:
    reader = csv.DictReader(csvfile)
    print len(reader)
    for row in reader:
        print row
"""
    print "type(reader) is %s" % type(reader)
    for row in reader:
        print "type(row) is %s" % type(row)
        for cell in row:
            print "type(cell) is %s" % type(cell)



#print "%s is %s" % (source_file, dialect)
"""