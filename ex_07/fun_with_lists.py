#!/usr/bin/python

from random import uniform


# Lists can hold anytihing
int_list = [1, 2, 3]
text_list = ['this', 'is', 'a', 'list', 'of', 'strings']

print int_list
print text_list

# You can make a list bigger or smaller
int_list.append(4)
int_list.remove(1)

print int_list

# You directly access a list's element by specifying the index of an item
print text_list[0] # should be 'this'

# you can iterate through a list
for item in text_list:
    print item

# you can grab a section
extract = text_list[3:6]
print extract


# In Python, lists can hold more than one type of thing
mixed_list_1 = [1, 'two', 3.0]
print mixed_list_1


# You can combine them
mixed_list_2 = int_list + text_list
print mixed_list_2
print "mixed_list_2 has a len of %d items." % len(mixed_list_2)


# You can map functions to a list
fifteen_zeros = [0 for i in range(15)]
fifteen_ones = [1] * 15

print fifteen_zeros
print fifteen_ones

# Let's build a list of random numbers
# This is a verbose way
my_list = list()
for number in range(0,4):
    my_list.append(uniform(1,100))

# This is more concise
my_list = [uniform(1,100) for i in range(0,4)]

# Applying some basics
print "List length is %d" % len(my_list)
print "List is %s" % my_list
print "Sorted list is %s" % sorted(my_list)
print "List sorted in reverse is %s" % sorted(my_list, reverse=True)
print "List elements are:"
for item in my_list:
    print "Index: %d, Item: %s" % (my_list.index(item), item)

# A list can be a list of lists
list_of_lists = [int_list, text_list, fifteen_ones, fifteen_zeros]
print list_of_lists

list_num = 0
print "Walking through the list of %d lists" % len(list_of_lists)
for a_list in list_of_lists:
    print "\tList %d has %d items:" % (list_num, len(a_list))
    index_num = 0
    for item in a_list:
        print "\t\tIndex %d has %s which is a(n) %s" % (index_num, item, type(item))
        index_num += 1 
    list_num += 1


"""
Read more at:
- http://effbot.org/zone/python-list.htm
- http://zetcode.com/lang/python/lists/
- http://www.tutorialspoint.com/python/python_lists.htm
- https://docs.python.org/2/tutorial/datastructures.html
"""