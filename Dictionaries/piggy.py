#!/usr/bin/env python

"""
Takes a logfile and computes the bandwidth users with the highest bandwidth 
usage
"""

import sys

def makeDict(logfile):
	# Create Empty Dict
	piggyDict = {}
	for lines in logfile:
		line =lines.strip().split(':')
		if line[0] in piggyDict:
			piggyDict[line[0]] += int(line[1])
		else:
			piggyDict[line[0]] = int(line[1])
	return piggyDict

def printReport(report):
	sortedKeys = sorted(report, key=report.get, reverse=True)
	print '=' * 40
	print "{0:<15}{1:>25}".format("IP Address", "Bytes")
	print '=' * 40
	for key in sortedKeys[:10]:
		print "{0:<15}{1:>25}".format(key, report[key])


if __name__ == "__main__":
	# Check to make sure there is a imput file on the command line
	if not len(sys.argv) > 1:
		print __doc__
		sys.exit(1)

	# See if its a valid file
	infile_name = sys.argv[1]
	try:
		infile = open(infile_name, 'r')
	except IOError:
		print "You must specify a valid file to parse"
		print __doc__
		sys.exit(1)

	# Create Dictionary
	report = makeDict(infile)
	printReport(report)