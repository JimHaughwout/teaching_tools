#!/usr/bin/python


def parse_them(items):
    for item in items:
        if item[0:3] == '$99':
            print "Yes: %r" % item
        else:
            print "No: %r" % item

items = ['$99avc','$99perpound', '$9', 'a', 'xyz123']
parse_them(items)

print items[99]


