#!/usr/bin/env python

import sys
import re

bibfile = "/home/mstefanc/publikacje/common/robot.bib"
infile = ""

if len(sys.argv) > 1:
    infile = sys.argv[1]
else:
	print "No input file"
	sys.exit
	
f = open(infile)
lines = f.read()

p = re.findall("\\citation{([^}]*)}*", lines)


bib = open(bibfile)
bibs = bib.read()

for e in set(p):
	p = re.search("^@[^{]*{%s,[^@]*"%(e), bibs, re.MULTILINE | re.DOTALL)
	print p.group()
