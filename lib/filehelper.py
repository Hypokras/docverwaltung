#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, subprocess

workdir = os.path.join(os.path.dirname(__file__), '..', 'ExampleFiles', 'workdir')

	
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
			
			makethumbabs(width, height, os.path.abspath(os.path.join(folder,currentfile)), os.path.abspath(os.path.join(thumbdir,thumbname)))
			#touch(os.path.join(thumbdir,thumbname))
		else:
			pass
	return returnvalue
	
	
	

##############
# count files in folder.
# return sum or false	
def count(folder):
	try:
		files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
	except:
		return False			
	return len(files)
##############
# Create thumbnail with relative size
# Return filename or False
def makethumbrel(width, height, source, destination):
	try:
		size = str(width)+"x"+str(height)
		p = subprocess.Popen(["convert", "-thumbnail", size, source, destination])
		p.communicate()
	except:
		return False
	return destination
##############
# Create thumbnail with absolute size
def makethumbabs(width, height, source, destination):
	try:
		size = str(width)+"x"+str(height)
		p = subprocess.Popen(["convert", "-resize", size, source, "-background", "none", "-gravity", "center", "-extent", size, destination])
		p.communicate()
	except:
		return False
	return destination
##############
# Rotate
def rotate(source, destination, rotation):
	try:
		p = subprocess.Popen(["convert", "-rotate", str(rotation), source, destination])
		p.communicate()
	except:
		return False
	return destination
	
##############
# Move
def move(source, destination):
	try:
		if not os.path.isfile(source):
			return False
		if not os.path.isdir(destionation)
			return False
		#move from a to b
		#delete thumbs
	
	
	
