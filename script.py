#!/usr/bin/python
import random
import time
import os
import sys

import fileinput


if len(sys.argv) < 2:
    print "script.py <namefile>"
    exit(1)
    
    
#for line in fileinput.input(sys.argv[1]):
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
i=0
for line in fileinput.input(sys.argv[1]):
	if(i!=0):
		words= line.split(";")
		nametrace=words[0]
		name=words[4]
		time=words[2]
		resource=words[5]+'/'+words[7]
		if(map.has_key(nametrace)):
			event=map[nametrace]
			event=event+generate_event(resource, "complete", name,time)
			map[nametrace]=event
		else:
			event=generate_event(resource, "complete", name,time)
			map[nametrace]=event
	i=i+1
		

		

	
def generate_trace(event,name):
    
    return """
	<trace>
		<string key="concept:name" value="%s"/>
		<string key="description" value="PaperOne"/>
                %s
        </trace>
""" % (name, event)	
		
def generate():
    print("""<?xml version="1.0" encoding="UTF-8" ?>
        <log xes.version="1.0" xes.features="nested-attributes" openxes.version="1.0RC7" xmlns="http://www.xes-standard.org/">
	<extension name="Lifecycle" prefix="lifecycle" uri="http://www.xes-standard.org/lifecycle.xesext"/>
	<extension name="Organizational" prefix="org" uri="http://www.xes-standard.org/org.xesext"/>
	<extension name="Time" prefix="time" uri="http://www.xes-standard.org/time.xesext"/>
	<extension name="Concept" prefix="concept" uri="http://www.xes-standard.org/concept.xesext"/>
	<extension name="Semantic" prefix="semantic" uri="http://www.xes-standard.org/semantic.xesext"/>
	<global scope="trace">
		<string key="concept:name" value="__INVALID__"/>
	</global>
	<global scope="event">
		<string key="concept:name" value="__INVALID__"/>
		<string key="lifecycle:transition" value="complete"/>
	</global>
	<classifier name="MXML Legacy Classifier" keys="concept:name lifecycle:transition"/>
	<classifier name="Event Name" keys="concept:name"/>
	<classifier name="Resource" keys="org:resource"/>
	<string key="source" value="Example One from Giorgio"/>
	<string key="concept:name" value="Paper"/>
	<string key="lifecycle:model" value="standard"/>
	<string key="description" value="Paper Submission"/>
       """)
    for key in map.keys():
    	event=map[key]
    	print generate_trace(event,key)
   
    print("""
        </log>
          """)

#NumeroRFC;Id;BeginDate;CategoriaRFC;Code;ChangeManager;ClasseRFC;Comp;FlowStatus;Richiedente;Stato;TipoRFC
#0			1  2         3			  4		5			6			7	8			9			10	 11


generate()	