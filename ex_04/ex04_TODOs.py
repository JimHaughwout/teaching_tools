#!/usr/bin/python
from sys import argv, exit
from datetime import datetime

### TODO: Make this whole program PEP-08 compliant

def isotime_from_strings(yyyymmdd, hhmmss):
    """
    Generates and returns IS0-8601 compliant date-time string (in UTC)
    from two input strings:
    - YYYYMMDD
    - HHMMSS

    Returns error if input strings are in invalid
    """
    ### TODO bring in common date formatting as utility function
    ### The reason is that we will use this in many places
    ### Let's use ISO-8601 format as this is an industry standard
    ### See https://en.wikipedia.org/wiki/ISO_8601
    ### Remember to delare the datetime object in UTC time zone


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
		## TODO: We only now need to parse and yyyymmdd = read[10:18] and ddmmss=read[18:24]
		date_yr = int(read[10:14]) # See Line 52
		date_mon = int(read[14:16]) # See Line 52
		date_day = int(read[16:18]) # See Line 52
		time_hr = int(read[18:20]) # See Line 52
		time_min = int(read[20:22]) # See Line 52
		time_sec = int(read[22:24]) # See Line 52
		# TODO replace the next line call to isotime_from_strings()
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
		# TODO: Replace next line simple print of dt (it is already a formated string!)
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
# We will move this to main() and use getopt in EX05
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