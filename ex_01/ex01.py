#!/usr/bin/python

from sys import argv, exit

if len(argv) != 2:
    print "Usage: %s file_to_read" % argv[0]
    exit(2)

infile = argv[1]

with open(infile, 'r') as source:
    print "### READING %s ###" % infile
    count = 0
    for row in source:
        count += 1
        print "Row %d is:\n%s" % (count, row)
    print "\n### DONE: Read and printed %d lines ###\n" % count 
