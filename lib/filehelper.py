#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess

workdir = os.path.join(os.path.dirname(__file__), '..', 'ExampleFiles', 'workdir')

def touch(path):
	with open(path, 'a'):
		os.utime(path, None)
        
def getFiles(folder):
	return os.listdir(folder)
	
def getConvertedFiles(folder, width, height, limit=10, contenttype="image/tiff"):
	returnvalue = []
	thumbdir = os.path.join(folder, 'thumbnails')
	if not os.path.isdir(thumbdir):
		os.makedirs(thumbdir)
	files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
	if limit < len(files):
		files = files[:limit]
	for currentfile in files:
	
		thumbname = currentfile.split(".")[0] + "_" + str(width) + "x" + str(height) + "." + contenttype.split("/")[1]
		currentthumbfile = os.path.relpath(os.path.abspath(os.path.join(thumbdir,thumbname)), os.path.join(workdir, '..'))
		returnvalue.append(currentthumbfile)
		if not os.path.isfile(os.path.join(thumbdir,thumbname)):
			
			makethumb(width, height, os.path.abspath(os.path.join(folder,currentfile)), os.path.abspath(os.path.join(thumbdir,thumbname)))
			#touch(os.path.join(thumbdir,thumbname))
		else:
			pass
	return returnvalue
	
def count(folder):
	files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
	return len(files)
	
def makethumb(width, height, source, destination):
	size = str(width)+"x"+str(height)
	p = subprocess.Popen(["convert", "-thumbnail", size, source, destination])
	p.communicate()
