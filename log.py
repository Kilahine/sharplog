#!/bin/bash/python
import csv
import os
import string
fname ="RDC.csv"
file = open(fname, "r")
write = open("test.csv","w")
nb=0
couleur=0
try:
	reader = csv.reader(file)
	for row in reader:
#		print '"'+row[1]+'", "' +row[2]+'", "' +row[5]+'", "' +row[7]+'", "'+row[8] +'"'
		if (row[5] > "2013-10-20T10:00") and (row[5] < "2013-10-29T10:00"):
			#	print '"'+row[1]+'", "' +row[2]+'", "' +row[5]+'", "' +row[7]+'", "'+row[8] +'"'
			write.write('"'+row[1]+'","' +row[2]+'","' +row[5]+'","' +row[7]+'","'+row[8] +'"\n')
finally:

	file.close()
	write.close()

file = open("test.csv")
try:
	reader = csv.reader(file)
	for row in reader:
		if (row[0] == "Impression") or (row[0]=="Copie"):
	
			print row
			nb=nb+int(row[3])
			couleur=couleur+int(row[4])
		
finally:
	file.close()
print "Impression nb =" + str(nb) +" Impression couleur = " + str(couleur)
