#!/bin/bash/python
import csv
import os
import string
fname ="RDC.csv"
file = open(fname, "r")

try:
	reader = csv.reader(file)
	for row in reader:
		print '"'+row[1]+'", "' +row[2]+'", "' +row[5]+'", "' +row[7]+'", "'+row[8] +'"'
		
finally:

	file.close()
