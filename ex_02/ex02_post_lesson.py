#!/usr/bin/python
from sys import argv, exit

# Check if we called this correctly
if len(argv) != 2:
	print "Usage: python ex01.py input_file"
	exit(2)


def parse_read(read):
	"""
	Takes in a read and detects the type. From the type routes to a parser
	"""
	if read[0:3] == '$99':
		parse_smoot(read)
	else:
		print "** Unknown Sensor Type ** - Read is:%s" % read


def parse_smoot(read):
	# Smoot Constants
	sensor_type = "Smoot"
	degreeChar = u'\u00b0' + 'C' # ask me why

	# Begin parse
	prologue = read[0:3]
	DeviceId = read[3:10]
	date_year = read[10:14]
	date_month = read[14:16]
	date_day = read[16:18]
	time_hour = read[18:20]
	time_minute = read[20:22]
	time_second = read[22:24]
	temp = float(read[24:27])/10.0 # Moved here. I will explain why
	checksum = read[27:31]

	# Print parse results
	print "prologue: %s" % (prologue)
	print "sensorType: %s" % sensor_type
	print "dateTime: %4s-%2s-%2s %2s:%2s:%2s" % (date_year, date_month, date_day, time_hour, time_minute, time_second)
	print "temperature: %f%s" % (temp, degreeChar)
	print "checksum: %s" % (checksum)
	##print "" ASK ME WHY
	print "\n-------------"


# Read in the file line-by-line and pass to the parser	
infile = argv[1]
print ""
print "### Reading %s ###" % (infile)
print ""
with open(infile) as data:
	count = 0
	for line in data:
		count += 1
		# print ""
		print "\nRow %s is:" % (count)
		parse_read(line)
print "### DONE: Read and printed %d lines of data ###" % (count) # Made %s into %d
