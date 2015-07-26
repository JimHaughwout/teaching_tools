#!/usr/bin/python
import csv

# Dictionaries let you 'lookup' an item (the value) the corresponses to 
# A thing in question (the key)

# One way to build a dict
person_dict_1 = {'first_name': 'John', 'last_name': 'Doe'}

# Another way
person_dict_2 = dict()
person_dict_2['first_name'] = 'Jane'
person_dict_2['last_name'] = 'Smith'

# You can print a whole dict
print person_dict_1
print person_dict_2

# Or just elements
print person_dict_1['first_name']
print person_dict_2['first_name']

# You can iterate through a dict
for key in person_dict_1:
    print "In person_dict_1, key=%s points to value=%s value" % (key, person_dict_1[key])


# Making a list of dicts is useful
phone_book = list()
phone_book.append({'first_name': 'John', 'last_name': 'Doe', 'phone': '705-555-1212'})
phone_book.append({'first_name': 'Jane', 'last_name': 'Doe', 'phone': '301-555-2121'})

# You can the interate thought value
for entry in phone_book:
    print "%s's number is %s" % (entry['first_name'], entry['phone'])

print phone_book[0].keys()


# This will be really useful later
with open('phone_book.csv', 'w') as target:
    field_names = phone_book[0].keys()
    writer = csv.DictWriter(target, field_names)
    writer.writeheader()
    for entry in phone_book:
        writer.writerow(entry)


"""
Read more:
- https://docs.python.org/2/tutorial/datastructures.html#dictionaries
- http://www.tutorialspoint.com/python/python_dictionary.htm
- http://www.dotnetperls.com/dictionary-python
"""