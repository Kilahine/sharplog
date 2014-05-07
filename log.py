#!/bin/bash/python
import sys
import csv
import os
import string


fname ="RDC.csv"
#file = open(fname, "r")
write = open("test.csv","w")
nb=0
couleur=0

if len(sys.argv) < 3:
	print "Usage : log.py NomduFichier.csv datedebut datefin "
	print "La date doit etre au format : 2012-06-23T10:00 "
	print "Annee-Mois-JourTheure:minute" 
	sys.exit(1)

primdate = sys.argv[2]
derdate = sys.argv[3]
CSV = sys.argv[1]
file = open(CSV,"r")
	
try:
	reader = csv.reader(file)
	for row in reader:
#		print '"'+row[1]+'", "' +row[2]+'", "' +row[5]+'", "' +row[7]+'", "'+row[8] +'"'
		if (row[5] > primdate) and (row[5] < derdate):
			#	print '"'+row[1]+'", "' +row[2]+'", "' +row[5]+'", "' +row[7]+'", "'+row[8] +'"'
			write.write('"'+row[1]+'","' +row[2]+'","' +row[5]+'","' +row[7]+'","'+row[8] +'"\n')
finally:

	file.close()
	write.close()

file = open("test.csv","r")
write = open("final.csv","w")
try:
	reader = csv.reader(file)
	for row in reader:
		if (row[0] == "Impression") or (row[0]=="Copie"):
			
			write.write('"'+row[0]+'","' +row[1]+'","' +row[2]+'","' +row[3]+'","'+row[4] +'"\n')
			nb=nb+int(row[3])
			couleur=couleur+int(row[4])
		
finally:
#	write.write("Impression nb =" + str(nb) +" Impression couleur = " + str(couleur))
	file.close()
	write.close()

file=open("final.csv","r")
liste = []
try:
	reader = csv.reader(file)
	for row in reader:
		if str(row[1]) not in liste:
			liste.append(row[1])
#		else:
#			print "Deja dans la liste"
finally:
	file.close()
#	print liste
	
#file=open("final.csv","r")
nb=0
couleur=0
rapport=open("Rapport.csv","w")
totalnb=0
totalcl=0
try:
	#reader = csv.reader(file)
	for i in liste:
		file=open("final.csv","r")
		reader = csv.reader(file)
#		rapport.write("Ordinateur : " + str(i) + " Noir et blanc : " + str(nb) + " couleur : " + str(couleur)+ "\n")
	#	print nb,couleur
	#	print i
		nb=0
		couleur=0
		for row in reader:
			if (i == row[1]):
			#	print "OK"	
				nb=nb+int(row[3])
				couleur=couleur+int(row[4])
				totalnb=totalnb+int(row[3])
				totalcl=totalcl+int(row[4])
					
		rapport.write("Ordinateur : " + str(i) + " Noir et blanc : " + str(nb) + " couleur : " + str(couleur)+ "\n")
		#	else:
			#	print "rien"
finally:
#	print nb,couleur
#	rapport.write("Ordinateur : " + str(i) + " Noir et blanc : " + str(nb) + " couleur : " + str(couleur)+ "\n")
	rapport.write(" Noir et blanc total : " + str(totalnb) + " Couleur : " + str(totalcl))
	file.close()
	rapport.close()
	os.remove("test.csv")
	os.remove("final.csv")
				
