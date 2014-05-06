#!/bin/bash/python
import csv
import os
import string
fname ="RDC.csv"
file = open(fname, "r")
write = open("test.csv","w")
try:
	reader = csv.reader(file)
	for row in reader:
#		print '"'+row[1]+'", "' +row[2]+'", "' +row[5]+'", "' +row[7]+'", "'+row[8] +'"'
		if (row[5] > "2012-12-29T10:00") and (row[5] < "2013-01-02T10:00"):
			#	print '"'+row[1]+'", "' +row[2]+'", "' +row[5]+'", "' +row[7]+'", "'+row[8] +'"'
			write.write('"'+row[1]+'","' +row[2]+'","' +row[5]+'","' +row[7]+'","'+row[8] +'"\n')
finally:

	file.close()
	write.close()
