#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

workdir = os.path.join(os.path.dirname(__file__), '..', 'ExampleFiles', 'workdir')

def touch(path):
	with open(path, 'a'):
		os.utime(path, None)
        
def getFiles(folder):
	return os.listdir(folder)
	
def getConvertedFiles(folder, width, height, limit=10, contenttype="image/tiff"):
	returnvalue = []
	thumpdir = os.path.join(folder, 'thumpnails')
	if not os.path.isdir(thumpdir):
		os.makedirs(thumpdir)
	files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
	if limit < len(files):
		files = files[:limit]
	for x in files:
	
		thumpname = x.split(".")[0] + "_" + str(width) + "x" + str(height) + "." + contenttype.split("/")[1]
		#thumpname = x[:len(x)-5] + "_" + str(width)+ "x" + str(height) + x[len(x)-5:]
		currentfile = os.path.relpath(os.path.abspath(os.path.join(thumpdir,thumpname)), os.path.join(workdir, '..'))
		returnvalue.append(currentfile)
		if not os.path.isfile(os.path.join(thumpdir,thumpname)):
			#hier sollte convertiert werden
			touch(os.path.join(thumpdir,thumpname))
		else:
			pass
	return returnvalue
	
