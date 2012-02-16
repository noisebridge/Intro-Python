#!/usr/bin/env python

"""
This script parses the apache logfile
useage piggies.py filename
"""

import sys

def makeDict(FileName):
	apacheRecords = {}
	for lines in FileName:
		line =lines.strip().split(':')
		if line[0] in apacheRecords:
			apacheRecords[line[0]] += int(line[1])
		else:
			apacheRecords[line[0]] = int(line[1])
	return apacheRecords

def printReport(records):
	sortedKeys = sorted(records, key=records.get)
	print '=' * 40
	print "{0:<15}{1:>25}".format("IP Address", "Bytes")
	print '=' * 40
	print sortedKeys
	for key in sortedKeys[:20]:
		print "{0:<15}{1:>25}".format(key, records[key])


if __name__ == '__main__':
	if not len(sys.argv) > 1:
		print __doc__
		sys.exit(1)

	inputFile = sys.argv[1]
	try:
		infile = open(inputFile, 'r')
	except IOError:
		print "You must specify a valid file to parse"
		print __doc__
		sys.exit(1)

	records = makeDict(infile)
	printReport(records)


	
