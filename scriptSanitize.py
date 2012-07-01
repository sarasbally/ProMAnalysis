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
   
#exit(1)
    
#for line in fileinput.input(sys.argv[1]): dd-MM-yyyy HH:mm
#	words= line.split(";")
#	for word in words:
		#print word

def generate_event(res, cicle, name,time):
	return """
	 <event>
              
              <string key="org:resource" value="%s"/>
              <string key="lifecycle:transition" value="%s"/>
              <string key="concept:name" value="%s"/>
              <date key="time:timestamp" value="%s"/>
              </event> 
""" % (res, cicle, name,time)
		
map={}
x=0
for line in spamReader:
	if x>0:
		words= line
		nametrace=words[0]
		name=words[4]
		#name = re.sub('\W','-', name)
		name = name.replace(' ', '-')
		name = name.replace('_', '-')
		name = name.replace('---', '-')
		name = name.replace('--', '-')
		#name = name.replace(' ', '-')
		time=words[2]
		time = time.replace('/','-')
		words[2]=time+':00'
		resource=words[5]+'/'+words[7]+'/'+words[9]
		words[4]=name
		i = len(words)
		for word in words:
			if i==1:
				print word
			else:
				sys.stdout.write(word+";")
			i=i-1;
	else:
		x=x+1
		i = len(header)
		for word in header:
			if i==1:
				print word
			else:
				sys.stdout.write(word+";")
			i=i-1;
		#if(name!=''):
		#	if(map.has_key(nametrace)):
		#		event=map[nametrace]
		#		event=event+generate_event(resource, "complete", name,time)
		#		map[nametrace]=event
		#	else:
		#		event=generate_event(resource, "complete", name,time)
		#		map[nametrace]=event
		
	
		

		

	
def generate_trace(event,name):
    
    return """
	<trace>
		<string key="concept:name" value="%s"/>
		<string key="description" value="PaperOne"/>
                %s
        </trace>
""" % (name, event)	
		

#NumeroRFC;Id;BeginDate;CategoriaRFC;Code;ChangeManager;ClasseRFC;Comp;FlowStatus;Richiedente;Stato;TipoRFC
#0			1  2         3			  4		5			6			7	8			9			10	 11

	

for key in map.keys():
    event=map[key]
    print generate_trace(event,key)