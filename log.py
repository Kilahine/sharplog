#!/bin/bash/python
import csv
import os
import string
fname ="RDC.csv"
file = open(fname, "r")

try:
	reader = csv.reader(file)
	for row in reader:
#		print '"'+row[1]+'", "' +row[2]+'", "' +row[5]+'", "' +row[7]+'", "'+row[8] +'"'
		if (row[5] > "2012-12-29T10:00") and (row[5] < "2013-01-02T10:00"):
				print '"'+row[1]+'", "' +row[2]+'", "' +row[5]+'", "' +row[7]+'", "'+row[8] +'"'
finally:

	file.close()
