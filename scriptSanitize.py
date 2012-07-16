#!/usr/bin/python
import random
import time
import os
import sys
import csv
from datetime import datetime
import fileinput
import re


if len(sys.argv) < 2:
    print "script.py <namefile>"
    exit(1)



spamReader = list(csv.reader(open(sys.argv[1],'U'), delimiter=';'))
header = spamReader[0]
#del spamReader[0]

def date_key(row):
        return datetime.strptime(row[2].strip(), "%d-%m-%Y %H:%M")


#spamReader.sort(key=date_key)

#for row in spamReader:
#	print row
#      writer = csv.writer(open("test1.csv", "wb"))
#      writer.writerows(row)
#print spamReader



map={}
x=0
for line in spamReader:
	if x>0:
		name=line[4]
		name = name.replace(' ', '-')
		name = name.replace('_', '-')
		name = name.replace('---', '-')
		name = name.replace('--', '-')
		#name = name.replace(' ', '-')
		time=line[2]
		time = time.replace('/','-')
		line[2]=time+':00'
		#resource=line[5]+'/'+line[7]+'/'+line[9]
		line[4]=name
		i = len(line)
		if len(name)>0:
			for word in line:
				if i==1:
					print word
				else:
					if i>4:
						sys.stdout.write(word+";")
				i-=1
	else:
		x += 1
		i = len(header)
		for word in header:
			if i==1:
				print word
			else:
				if i>4:
					sys.stdout.write(word+";")
			i-=1





#NumeroRFC;Id;BeginDate;CategoriaRFC;Code;ChangeManager;ClasseRFC;Comp;FlowStatus;Richiedente;Stato;TipoRFC
#0			1  2         3			  4		5			6			7	8			9			10	 11



#for key in map.keys():
 #   event=map[key]
 #   print generate_trace(event,key)
