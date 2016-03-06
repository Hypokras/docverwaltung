#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


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
		return """\
{
	"meta": {
		"error": 1,
		"error_message": "not yet implemented...",
		"version": "0.0.1"
	}
}
		"""








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
		

