#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json
import filehelper


workdir = os.path.join(os.path.dirname(__file__), '..', 'ExampleFiles', 'workdir')


# Message example:
"""
{
	"meta": {
	"version": "0.0.1",
	"content-type": "image/tiff",
	"limit": 10,
	"start": 0,
	"store": "queue",
	"width": 106,
	"height": 150,
	"action": "list",
	"parameter": {}
	}
}
"""
def validate(message):
	contenttype = ['image/tiff']
	limit = [1, 999]
	store = os.listdir(workdir)
	width = [1, 2550]
	height = [1, 3300]
	action = ['list']
	error_message = ""
	
	if not message['meta']['content-type'] in contenttype:
		error_message = error_message + ", Unknown content-type: " + message['meta']['content-type']
		
	if not message['meta']['limit'] in range(limit[0], limit[1]):
		error_message = error_message + ", Limit out of range: " + str(message['meta']['limit'])
	
	if not message['meta']['store'] in store:
		error_message = error_message + ", Unknown store: " + message['meta']['store']
		
	if not message['meta']['width'] in range(width[0], width[1]):
		error_message = error_message + ", Width out of range: " + str(message['meta']['width'])
		
	if not message['meta']['height'] in range(height[0], height[1]):
		error_message = error_message + ", Height out of range: " + str(message['meta']['height'])
	
	if not message['meta']['action'] in action:
		error_message = error_message + ", Unknown action: " + message['meta']['action']
	return error_message
		
		
def dosomething(message):
	validationresult = validate(message)
	if validationresult:
		return """\
{
	"meta": {
		"error": 1,
		"error_message": "Validation failed: %s",
		"version": "0.0.1"
	}
}
		"""	%validationresult
		
	if message['meta']['action'] == "list":
	
		store = os.path.join(workdir, message['meta']['store'])
		files = filehelper.getConvertedFiles(store, message['meta']['width'], message['meta']['height'], limit=message['meta']['limit'])
		if files:
			template = dict()
			template['meta'] = dict()
			template['items'] = dict()
			template['meta']['error'] = 0
			template['meta']['version'] = "0.0.1"
			template['meta']['length'] = len(files)
			template['meta']['start'] = message['meta']['start']
			template['meta']['limit'] = message['meta']['limit']
			template['meta']['action'] = message['meta']['action']
			template['meta']['fields'] = ['width','height','store','content-type']
			
			for x in files:
				template['items'][x] = [message['meta']['width'], message['meta']['height'], message['meta']['store'], message['meta']['content-type']]
			return json.dumps(template)
		else:
			return """\
{
	"meta": {
		"error": 1,
		"error_message": "no files found in %s",
		"version": "0.0.1"
	}
}
			""" %store


	else:
		return """\
{
	"meta": {
		"error": 1,
		"error_message": "unknown action: %s",
		"version": "0.0.1"
	}
}
		"""	%message['meta']['action']
		

