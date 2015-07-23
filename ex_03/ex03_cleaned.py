#!/usr/bin/python
from sys import argv, exit
from datetime import datetime

def parse_read(read):
	"""
	Takes in a read and detects the type. From the type routes to a parser
	"""
	prologue = read[0:3] # Declaring this makes all following code easier to read

	if prologue == '$99':
		parse_smoot(read)
	
	elif prologue == '$69':
		print "** Sorry, have not added Cobra yet for %r" % read
	
	else:
		print "** Unknown Sensor Type ** - Read is: %r" % read


def parse_smoot(read):
	"""
	Takes in a generic read, parses and prints a parses Smoot
	Returns errors if data are not in valid format
	"""
	sensor_type = 'Smoot'
	SMOOT_PROLOGUE = '$99' # This is Constant
	degreeChar = u'\u00b0' + 'C'
	
	try:
		# First try to parse data into features
		prologue = read[0:3]
		DeviceId = read[3:10]
		date_yr = int(read[10:14]) # Can cast this now as we are using datetime library
		date_mon = int(read[14:16]) # BTW, casting here will raise int case value errors
		date_day = int(read[16:18])
		time_hr = int(read[18:20])
		time_min = int(read[20:22])
		time_sec = int(read[22:24])
		dt = datetime(date_yr, date_mon, date_dy, time_hr, time_min, time_sec)
		temp = float(read[24:27])/10.0 
		checksum = read[27:31]
		
		# Now check this is actually a Smooth. If not exit the function
		if prologue != SMOOT_PROLOGUE:
			print "Did not send Smoot message, sent:\n%r" % read
			return

		# Now print the Smoot
		print "prologue: %s" % prologue
		print "sensorType: %s" % sensor_type
		print dt.strftime("dateTime: %m/%d/%Y %I:%M:%S") # No need to try/except as line 41 already creates a dt (or throws an exception)
		print "temperature: %f%s" % (temp, degreeChar)
		print "checksum: %s" % checksum
		print "\n-------------"
	
	except ValueError:
		print "Invalid Smoot read:\n%r" % (read)
		print ValueError

"""
This is pretty much the 'main' program
"""
# Check if the correct arguments were passed on invocation
if len(argv) != 2:
	print "Usage: python %s input_file" % argv[0] # Using this lets us print the correct output even if filename is changed
	exit(2)
infile = argv[1]  

print "\n### Reading %s ###\n" % infile

# Read in the file line-by-line and pass to the parser	
with open(infile) as data:
	count = 0
	for line in data:
		count += 1
		print "\nRow %d is:" % count # Use %d, not %s
		parse_read(line)

print "\n### DONE: Read and printed %d lines of data ###\n" % count