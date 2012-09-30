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
lungheader=len(header)
x=1
for line in spamReader:
	l= len(line)
	if l!=lungheader:
		print x ," ",l ," ",lungheader, " ",l-lungheader
	x=x+1