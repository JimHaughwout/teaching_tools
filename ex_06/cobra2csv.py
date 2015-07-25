#!/usr/bin/python
"""
This script reads in a file of smf-universal-reads and extracts some info
into a target CSV for easy debugging. It is primarily used for debugging 
tag mapping.

TODO - Make this less klunky. It is still rather hacky
"""
import sys
import json
import csv
import getopt

def print_usage_and_exit(msg=None):
    """ 
    Pretty print exit on error
    """
    print "\nUsage: %s [-s][-h]" % sys.argv[0]
    print "\t-h Print usage help"
    print "\t-s Source accumulated smurfs file (Required)"
    if msg: print msg + "\n"
    sys.exit(2)


def try_dict_extract(dictionary, key_list):
    """
    Iterates through a list of keys to try to return a dictionary key value.
    On exception, returns NoneType
    """
    try:
        x = dictionary
        for key in key_list:
            x = x[key]
        return x
    except:
        return None


def extract_smurf(row):
    """
    Check if data is in SMF2 format AND is a SMurF. If not exits with error
    """
    try: 
        smurf = json.loads(row)
        if smurf['smfMetaData']['payloadType'] != 'smf-universal-read':
            print_usage_and_exit(("%r is not a SMurF" % row))
        return smurf
    except (ValueError, KeyError, TypeError) as e:
        print_usage_and_exit(("%r is not even in SMF2 format: %s" % (row, e)))


def check_for_event(smurf_obj, event_name):
    """
    Trys to determine event exists in smfPayloadData['events'] 
    If so, returns a 1 (else None)
    TODO: May make a generic list of events to return
    """
    key_list = ['smfPayloadData', 'events']
    key_list.append(event_name)
    if try_dict_extract(smurf_obj, key_list) == None:
        return None
    else: 
        #return event_name
        return 1


# Parse opts, ensure we have required opts to determine mode, source, target
try:
    opts, args = getopt.getopt(sys.argv[1:], "hs:")
    if not opts:
        print_usage_and_exit('No options supplied')
except getopt.GetoptError:
    print_usage_and_exit('Could not parse options')

for opt, arg in opts:
    if opt == '-h':
        print_usage_and_exit()      
    elif opt == '-s':
        infile = arg

if not(infile):
    print_usage_and_exit('-s source_file not specified')
outfile = 'extract_' + infile + '.csv'


# Try to open source file and extact events
try:
    source = open(infile, 'r')
    event_list = source.readlines()
    source.closed
except IOError as e:
    print_usage_and_exit(("Could not open %r to read: %s" % (infile, e)))


# Try to open target file and write CSV headers
try:
    target = open(outfile, 'w')
    writer = csv.writer(target)
    writer.writerow(['sensor', 'utc_timestamp', 'ack', 'battery_level',
        'latitude', 'longitude', 'accuracy', 
        't1_mcc', 't1_mnc', 't1_lac', 't1_cell_id',' t1_ss', 't1_type',
        't2_mcc', 't2_mnc', 't2_lac', 't2_cell_id',' t2_ss', 't2_type',
        't3_mcc', 't3_mnc', 't3_lac', 't3_cell_id',' t3_ss', 't3_type',
        'unresolvedLocationSensor', 'noLocationSensor', 'lowBattery',
        'smfMsgId', 'parentSmfMsgId'
        ])
except IOError as e:
    print_usage_and_exit(("Could not open %r to write: %s" % (outfile, e)))


# Loop through events, parse into a data row, then write data row to CSV
event_count = 0

for event in event_list:
    smurf = extract_smurf(event)
    data = list()

    data.append(try_dict_extract(smurf, ['smfMetaData', 'deviceId']))
    data.append(try_dict_extract(smurf, ['smfPayloadData', 'timestamp']))
    data.append(try_dict_extract(smurf, ['smfMetaData', 'endpointResponseCode']))
    data.append(try_dict_extract(smurf, ['smfPayloadData', 'measures', 'batteryLevel', 'maxPct']))
    data.append(try_dict_extract(smurf, ['smfPayloadData', 'position', 'gps', 'latitude']))
    data.append(try_dict_extract(smurf, ['smfPayloadData', 'position', 'gps', 'longitude']))
    data.append(try_dict_extract(smurf, ['smfPayloadData', 'position', 'gps', 'accuracy']))

    try:
        for tower in smurf['smfPayloadData']['position']['gps']['towers']:
            data.append(try_dict_extract(tower, ['mobileCountryCode']))
            data.append(try_dict_extract(tower, ['mobileNetworkCode']))
            data.append(try_dict_extract(tower, ['locationAreaCode']))
            data.append(try_dict_extract(tower, ['cellId']))
            data.append(try_dict_extract(tower, ['signalStrength']))
            data.append(try_dict_extract(tower, ['cellType']))
    except:
        for item in range(0,9):
            data.append(None)

    data.append(check_for_event(smurf, 'unresolvedLocationSensor'))
    data.append(check_for_event(smurf, 'noLocationSensor'))
    data.append(check_for_event(smurf, 'lowBattery'))

    data.append(try_dict_extract(smurf, ['smfMetaData', 'smfMessageId']))
    data.append(try_dict_extract(smurf, ['smfMetaData', 'smfParentMessageId']))
    
    writer.writerow(data)
    event_count += 1

# Tell user done and print stats
print "SUCCESS: Process %d events. Created %s" % (event_count, outfile)