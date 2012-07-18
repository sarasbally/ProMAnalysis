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

numline=0
if len(sys.argv)==3:
	numline=int(sys.argv[2])
else:
	numline=2000
	#exit(1)

spamReader = list(csv.reader(open(sys.argv[1]), delimiter=';'))
end=0
for line in spamReader:
	if end<numline:
		i = len(line)
		for word in line:
			if i==1:
				print word
			else:
				sys.stdout.write(word+";")
			i-=1
	end+=1
