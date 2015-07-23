#!/usr/bin/python
from sys import argv, exit
import getopt

def print_usage_and_exit(msg=None):
    """
    Prints Usage help and any error messages and exits
    """
    print "\nUsage: %s [-h][-d][-u]" % argv[0]
    print "\t-h\tPrint usage help and exit (Optional)"
    print "\t-d\tDeviceId to use (Defaults to Foo0123456789A if not provided)"
    print "\t-n\tNumber to show (Optional. Show ALL if not specified)"
    print "\t-s\tSource data file (Required)"
    print "\t--v\tRun in verbose mode (Optional, defaults to non-verbose)"
    if msg: 
        print '\n' + msg + '\n'
    exit(2)


def parse_options(argv):
    """
    TODO
    """
    # First see if opts are even parseable. If not, exit
    try:
        opts, args = getopt.getopt(argv, "hd:n:s:", ['v'])
        if not opts:
            print_usage_and_exit('No options supplied')
    except getopt.GetoptError:
        print_usage_and_exit('Could not parse options')    

    # Now initialize the option variables. 
    # Set these to default values if they exist. Otherwise set to None
    device = 'Foo0123456789A'
    infile = None
    outfile_extension = '_out.txt'
    num_to_show = None
    verbose = False

    # Now set the option vars based on what was passed
    for opt, arg in opts:
        if opt == '-h':
            print_usage_and_exit()
        elif opt == '-d':
            device = arg
        elif opt == '-n':
            num_to_show = arg     
        elif opt == '-s':
            infile = arg
        elif opt == '--v':
            verbose = True

    # Now check if required options are set. If not, default or exit
    if not(device):
        print_usage_and_exit('-d device IMEI not specified')

    try:
        num_to_show = int(num_to_show)
    except:
        num_to_show = None # Which means I show ALL 

    if not(infile): # Fault tolerance if we set default device to None
        print_usage_and_exit('-s source_file not specified')
    outfile = device + outfile_extension

    if not(verbose): # Force to False if not specified
        verbose = False  

    # Return
    return infile, outfile, device, num_to_show, verbose


def main(argv):
    """Main method"""
    # This is all you need to parse options
    # It returns the value needed
    infile, outfile, device_id, num_to_show, verbose = parse_options(argv)

    # Now you can simply proceed as if the option variable are defined
    # As an example, I just printed stuff
    print "Input file: %s" % infile
    print "Output file: %s" % outfile
    print "Device %s" % device_id
    if num_to_show:
        print "Showing only %d item(s)" % num_to_show
    else: 
        print "Showing all items"
    if verbose:
        print "Running in Verbose Mode"
    else:
        print "Not running in Verbose Mode"


""" This is needed to wrap the whole script in a shell """
if __name__ == '__main__':
    main(argv[1:])